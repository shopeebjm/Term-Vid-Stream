# vid-term (Terminal Video Streamer)

`vid-term` is a high-performance, interactive Python CLI tool that allows you to stream video and live webcam feeds directly in your terminal using ASCII characters. It features real-time frame resizing, audio synchronization, and direct YouTube streaming support.

## Features

- **High-FPS ASCII Rendering:** Utilizes OpenCV and Numpy's advanced vectorized operations to instantly map video frames to ASCII luminance values.
- **Full Terminal Scaling:** Videos stretch and adapt to perfectly fill your terminal's height and width.
- **Flicker-Free Playback:** Uses ANSI cursor repositioning instead of clearing the screen to guarantee smooth video without terminal tearing.
- **Audio Sync:** Plays audio seamlessly in the background (headless) using `ffplay` for local files and YouTube streams.
- **Webcam Support:** Instantly maps your local webcam feed fully into the terminal.
- **YouTube Support:** Integrates with `yt-dlp` to extract and stream YouTube videos natively.
- **Interactive Menu:** A beautiful, easy-to-use menu using `inquirer` for quick source selection.

## Prerequisites

Before running `vid-term`, make sure you have the following installed on your system:
- **Python 3.7+**
- **FFmpeg:** Required for audio playback and YouTube extraction.
  - *Windows:* Install via `winget install ffmpeg` or download binaries from [gyan.dev](https://www.gyan.dev/ffmpeg/builds/). Ensure it is in your system PATH.

## Installation

1. Clone or download this repository.
2. Navigate to the project directory:
   ```bash
   cd vid-term
   ```
3. Set up a Python Virtual Environment:
   ```bash
   python -m venv venv
   # On Windows:
   .\venv\Scripts\activate
   # On macOS/Linux:
   source venv/bin/activate
   ```
4. Install the required Python packages:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

### Interactive Menu (Recommended)
Simply run the script with no arguments to bring up the interactive source selection menu:
```bash
python vid_term.py
```

### Direct Commands
You can bypass the menu by passing arguments directly:

**Stream your Webcam:**
```bash
python vid_term.py --webcam
```

**Stream a Local Video File:**
```bash
python vid_term.py /path/to/your/video.mp4
```

**Stream a YouTube Video:**
```bash
python vid_term.py https://www.youtube.com/watch?v=dQw4w9WgXcQ
```

*Note: Press `Ctrl+C` inside the terminal window at any time to gracefully stop the video and audio playback.*

## Dependencies
- `opencv-python`: High-performance video capture and frame resizing.
- `numpy`: Lightning-fast vectorized math for ASCII conversion.
- `yt-dlp`: Extracting direct video/audio stream URLs from YouTube.
- `inquirer`: Providing the interactive terminal UI.

## Troubleshooting

- **No Audio playing:** Ensure `ffmpeg` and `ffplay` are installed and accessible in your system's PATH variable.
- **YouTube URL extraction errors:** Make sure you are using the latest version of `yt-dlp` (run `pip install --upgrade yt-dlp`) as YouTube frequently changes their backend. Some live streams or DRM-protected videos may not work.
- **Performance Issues:** Ensure your terminal emulator supports hardware acceleration (like Windows Terminal, Alacritty, or Kitty) for the best framerates when rendering massive blocks of ASCII characters.
