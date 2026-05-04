import argparse
import sys
import os
import cv2
import numpy as np
import time
import subprocess
import re
import urllib.parse
import inquirer
import atexit

ASCII_CHARS = " .:-=+*#%@"
NUM_CHARS = len(ASCII_CHARS)

# Global reference to audio process so we can kill it on exit
audio_process = None

def cleanup_audio():
    global audio_process
    if audio_process:
        try:
            audio_process.terminate()
            audio_process.wait(timeout=1)
        except:
            pass

atexit.register(cleanup_audio)

def get_terminal_size():
    # Attempt to get terminal size, default to 80x24 if it fails.
    try:
        columns, lines = os.get_terminal_size()
        return columns, lines
    except OSError:
        return 80, 24

def parse_args():
    parser = argparse.ArgumentParser(description="Terminal Video Streamer (vid-term)")
    parser.add_argument("source", nargs="?", default=None, help="Path to video file, YouTube URL, or 'live' for webcam.")
    parser.add_argument("--webcam", action="store_true", help="Use webcam as source (equivalent to 'live')")
    parser.add_argument("--color", action="store_true", help="Enable ANSI true color rendering.")
    return parser.parse_args()

def is_youtube_url(url):
    youtube_regex = r'(https?://)?(www\.)?(youtube|youtu|youtube-nocookie)\.(com|be)/(watch\?v=|embed/|v/|.+\?v=)?([^&=%\?]{11})'
    return bool(re.match(youtube_regex, str(url)))

def get_youtube_stream_urls(url):
    print(f"Extracting stream URLs for {url} using yt-dlp...")
    try:
        # Request best video and best audio separately for ffplay compatibility
        result = subprocess.run(
            ['yt-dlp', '-g', '-f', 'bestvideo[height<=720]', url],
            capture_output=True, text=True, check=True
        )
        vid_url = result.stdout.strip().split('\n')[0]
        
        result_audio = subprocess.run(
            ['yt-dlp', '-g', '-f', 'bestaudio', url],
            capture_output=True, text=True, check=True
        )
        aud_url = result_audio.stdout.strip().split('\n')[0]
        
        return vid_url, aud_url
    except subprocess.CalledProcessError as e:
        print(f"Error extracting YouTube URL: {e.stderr}")
        return None, None
    except FileNotFoundError:
         print("Error: yt-dlp not found. Make sure it is installed and in your PATH.")
         return None, None

def process_frame(frame, cols, rows):
    # Resize frame to fit terminal
    # Terminal characters are typically roughly twice as tall as they are wide
    max_w = cols
    max_h = rows - 1
    
    # Force the frame to use the full width and available height of the terminal
    # Stretching it slightly to remove "black bars" on the sides
    new_w = max_w
    new_h = max_h
        
    if new_w <= 0 or new_h <= 0:
        return ""
        
    resized = cv2.resize(frame, (new_w, new_h))
    
    # Convert to grayscale for luminance
    gray = cv2.cvtColor(resized, cv2.COLOR_BGR2GRAY)
    
    # Normalize and map to ASCII characters
    normalized = (gray / 255.0) * (NUM_CHARS - 1)
    indices = np.round(normalized).astype(int)
    
    # Create the ascii string using Numpy's advanced indexing
    ascii_frame = np.array(list(ASCII_CHARS))[indices]
    
    # Join rows with newlines
    lines = ["".join(row) for row in ascii_frame]
    return "\n".join(lines)

def start_audio(audio_source):
    global audio_process
    try:
        # Using ffplay from the ffmpeg suite to play audio in the background (headless)
        audio_process = subprocess.Popen(
            ['ffplay', '-nodisp', '-autoexit', '-loglevel', 'quiet', audio_source],
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL
        )
    except FileNotFoundError:
        print("Warning: ffplay not found. Audio will not play. Install ffmpeg to enable audio.")

def stream_video(video_source, audio_source=None):
    cap = cv2.VideoCapture(video_source)
    
    if not cap.isOpened():
        print(f"Error: Could not open source {video_source}")
        return
        
    fps = cap.get(cv2.CAP_PROP_FPS)
    if fps <= 0 or np.isnan(fps):
        fps = 30.0
        
    frame_delay = 1.0 / fps
    
    # Start audio slightly before video rendering begins
    if audio_source:
        start_audio(audio_source)
    
    # Clear screen once at the beginning
    sys.stdout.write("\033[2J")
    
    try:
        while True:
            start_time = time.time()
            
            ret, frame = cap.read()
            if not ret:
                break
                
            cols, rows = get_terminal_size()
            ascii_str = process_frame(frame, cols, rows)
            
            # Move cursor to top left instead of clearing screen to prevent flickering
            sys.stdout.write("\033[H" + ascii_str)
            sys.stdout.flush()
            
            # Maintain FPS limit
            elapsed = time.time() - start_time
            sleep_time = frame_delay - elapsed
            if sleep_time > 0:
                time.sleep(sleep_time)
                
    except KeyboardInterrupt:
        pass
    finally:
        cap.release()
        cleanup_audio()
        sys.stdout.write("\n")

def interactive_menu():
    questions = [
        inquirer.List('source_type',
                      message="What do you want to stream?",
                      choices=['Webcam (Live)', 'YouTube Video', 'Local Video File', 'Exit'],
                  ),
    ]
    answers = inquirer.prompt(questions)
    
    if answers is None or answers['source_type'] == 'Exit':
        sys.exit(0)
        
    choice = answers['source_type']
    
    if choice == 'Webcam (Live)':
        return 0
    elif choice == 'YouTube Video':
        url_q = [inquirer.Text('url', message="Enter the YouTube URL")]
        url_ans = inquirer.prompt(url_q)
        if url_ans and url_ans['url']:
            return url_ans['url']
        return None
    elif choice == 'Local Video File':
        file_q = [inquirer.Text('file', message="Enter the path to the local video file")]
        file_ans = inquirer.prompt(file_q)
        if file_ans and file_ans['file']:
            return file_ans['file']
        return None
        
    return None

def main():
    args = parse_args()
    
    source = None
    
    if args.webcam:
        source = 0
    elif args.source:
        source = args.source
    else:
        # Launch interactive menu if no arguments are provided
        source = interactive_menu()
        if source is None:
            return
            
    audio_source = None
    
    if source == "live":
        source = 0  # 0 is usually the default webcam index in OpenCV
    elif isinstance(source, str):
        if is_youtube_url(source):
            vid_extracted, aud_extracted = get_youtube_stream_urls(source)
            if vid_extracted:
                source = vid_extracted
                audio_source = aud_extracted
            else:
                print("Failed to extract YouTube stream.")
                return
        else:
            # If it's a local file, the audio source is the same file
            audio_source = source

    print(f"Opening source...")
    stream_video(source, audio_source)

if __name__ == "__main__":
    if os.name == 'nt':
        # Enable ANSI escape sequence parsing in Windows terminal
        os.system('color')
    main()
