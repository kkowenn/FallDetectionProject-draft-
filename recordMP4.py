# MacOS and this just one video
import subprocess
from datetime import datetime

def capture_webcam_ffmpeg():
    # Define the path and filename for the output
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    save_path = f'/Users/kritsadakruapat/Desktop/project/recorded_video/recorded_{timestamp}.mp4'

    # Set up the FFmpeg command for recording video from webcam
    command = [
        'ffmpeg',
        '-f', 'avfoundation',  # Input format for macOS (use 'v4l2' for Linux)
        '-framerate', '30',    # Frame rate
        '-i', '0',             # Input device number for the default webcam
        '-t', '5',             # Duration in seconds
        '-pix_fmt', 'yuv420p', # Pixel format for compatibility
        '-vcodec', 'libx264',  # Video codec
        '-preset', 'fast',     # Encoding speed/quality trade-off
        '-crf', '23',          # Constant Rate Factor for quality
        '-vf', 'scale=1280:-2',# Scaling to width 1280 pixels, keep aspect ratio
        save_path
    ]

    # Start the FFmpeg recording process
    process = subprocess.Popen(command, stderr=subprocess.PIPE, stdout=subprocess.PIPE)
    stdout, stderr = process.communicate()

    if process.returncode == 0:
        print(f"Video successfully saved to {save_path}")
    else:
        print(f"Error saving video: {stderr.decode()}")

if __name__ == '__main__':
    capture_webcam_ffmpeg()


