# Term-Vid-Stream (Terminal Video Streamer)

<img src="https://readme-typing-svg.herokuapp.com?color=%2336BCF7&center=true&vCenter=true&lines=TikTok+@shopee.bjm" />
</p>
<p align="center">
<img src="https://readme-typing-svg.herokuapp.com?color=%2336BCF7&center=true&vCenter=true&lines=s+h+o+p+e+e+b+j+m" />
</p>

<h2 align="center">
  
[![Powered By:shopeebjm](https://img.shields.io/badge/PoweredBy:shopeebjm-7%2B-blue.svg?style=flat)](http://linktr.ee/kiplymacho)

# Deskripsi
`Term-Vid-Stream` adalah alat CLI Python interaktif berkinerja tinggi yang memungkinkan Anda untuk melakukan streaming video dan umpan webcam langsung di terminal Anda menggunakan karakter ASCII. Fitur-fiturnya meliputi pengubahan ukuran frame secara real-time, sinkronisasi audio, dan dukungan streaming langsung ke YouTube.

# Fitur
- **Rendering ASCII FPS Tinggi:** Memanfaatkan operasi vektorisasi canggih OpenCV dan Numpy untuk memetakan frame video ke nilai luminansi ASCII secara instan.
- **Penskalaan Terminal Penuh:** Video meregang dan beradaptasi untuk mengisi tinggi dan lebar terminal Anda dengan sempurna.
- **Pemutaran Bebas Kedip:** Menggunakan penempatan ulang kursor ANSI alih-alih membersihkan layar untuk menjamin video yang lancar tanpa gangguan gambar.
- **Sinkronisasi Audio:** Memutar audio secara lancar di latar belakang (headless) ffplayuntuk file lokal dan streaming YouTube.
- **Dukungan Webcam:** Secara instan memetakan tampilan webcam lokal Anda sepenuhnya ke dalam terminal.
- **Dukungan YouTube:** Terintegrasi yt-dlpuntuk mengekstrak dan menayangkan video YouTube secara langsung.
- **Menu Interaktif:** Menu yang indah dan mudah digunakan inquireruntuk pemilihan sumber yang cepat.

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

# Social Media

<h2 align="center">

[![shopee](https://img.shields.io/badge/shopee-200%2B-yellow.svg?style=flat)](https://shopee.co.id/infinixnote40bjm)

[![Youtube shopee_banjarmasin](https://img.shields.io/badge/YouTube-200%2B-yellow.svg?style=flat)](https://www.youtube.com/@shopee_banjarmasin)

[![Instagram shopee_banjarmasn](https://img.shields.io/badge/Instagram-2K%2B-yellow.svg?style=flat)](https://www.instagram.com/shopee_banjarmasin)

[![Twitter KipyMacho](https://img.shields.io/badge/Twitter-350%2B-yellow.svg?style=flat)](https://www.twitter.com/shopeebjm)
  
[![Tiktok Shopeebjm](https://img.shields.io/badge/TikTok-80%2B-yellow.svg?style=flat)](https://www.tiktok.com/@shopee.bjm)

[![Facebook shopee.bjm](https://img.shields.io/badge/Facebook-199%2B-yellow.svg?style=flat)](https://www.facebook.com/shopee.bjm)

[![Telegram](https://img.shields.io/badge/Telegram-77%2B-yellow.svg?style=flat)](http://t.me/shopeebjm)

[![LinkedIn](https://img.shields.io/badge/LinkedIn-80%2B-yellow.svg?style=flat)](http://www.linkedin.com/in/kiplymacho)

</p>
<div height='45' align="center">
<h2>Contact me: <br>
<a href="https://github.com/shopeebjm"> <img src="https://cdn.jsdelivr.net/npm/simple-icons@3.0.1/icons/github.svg" height='50'> </a>
<a href="https://facebook.com/shopee.bjm"> <img src="https://cdn.jsdelivr.net/npm/simple-icons@3.0.1/icons/facebook.svg" height='50'> </a>
  
<a href="https://paypal.me/kiplymacho"> <img src="https://cdn.trakteer.id/images/embed/trbtn-red-6.png" height='50'> </a>
</h2>
</div>

# Follow Me :
‎‎[![Messenger](https://img.shields.io/badge/Messengers-blue?style=for-the-badge&logo=messenger)](https://fb.me/shopee.bjm)
‎<a href="https://tiktok.com/@shopee.bjm"><img title="TikTok" src="https://img.shields.io/badge/-black?style=for-the-badge&logo=Tiktok"></a>
‎<a href="https://linktr.ee/kiplymacho" target="_blank"><img src="https://img.shields.io/badge/Socials-grey?style=for-the-badge&logo=linktree"></a>
‎<a href="https://github.com/shopeebjm" target="_blank"><img src="https://img.shields.io/badge/Github-blue?style=for-the-badge&logo=github"></a>
‎</p>
‎‎[![Instagram](https://img.shields.io/badge/Instagram-Follow-red?style=for-the-badge&logo=instagram)](https://instagram.com/shopee_banjarmasin)
‎[![Blog](https://img.shields.io/badge/Website-Visit-yellow?style=for-the-badge&logo=blogger)](https://kiplymacho.blogspot.com)
‎[![Facebook](https://img.shields.io/badge/Facebook-Like-red?style=for-the-badge&logo=facebook)](https://facebook.com/shopee.bjm)
‎[![HalamanFacebook](https://img.shields.io/badge/Halaman-Facebook-sky?style=for-the-badge&logo=facebook)](https://facebook.com/httpcustomkiplymacho)
‎[![WhatsApp](https://img.shields.io/badge/WhatsApp-red?style=for-the-badge&logo=whatsapp)](https://wa.me/6285751032225)
‎[![Telegram](https://img.shields.io/badge/Forum-Diskusi-blue?style=for-the-badge&logo=forum)](https://t.me/shopeebjm)
‎<a href="https://youtube.com/@shopee_banjarmasin"><img title="YouTube" src="https://img.shields.io/badge/YouTube-@Shopee_Banjarmasin-red?style=for-the-badge&logo=Youtube"></a>
