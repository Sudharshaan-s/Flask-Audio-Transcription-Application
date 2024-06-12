# Flask Audio Transcription Application

This is a Flask-based web application that allows users to upload audio files (MP3, WAV) and transcribe the audio content using Google's Speech Recognition API.

## Features

- Upload audio files in MP3 or WAV format.
- Convert MP3 files to WAV format using `pydub` and `ffmpeg`.
- Transcribe audio content using `speech_recognition` library and Google's Speech API.
- Display the transcribed text on the web page.

## Installation

### Prerequisites

- Python 3.7+
- Flask
- pydub
- speech_recognition
- ffmpeg

### Setup

1. Clone the repository:

   ```sh
   git clone https://github.com/yourusername/your-repo.git
   cd your-repo
