import subprocess
import os


def download_audio(url):
    output_template = "%(title)s.%(ext)s"
    subprocess.run(
        [
            "yt-dlp",
            "-x",
            "--audio-format",
            "mp3",
            "--no-progress",
            "-o",
            output_template,
            url,
        ],
        check=True,
    )
    for f in os.listdir("."):
        if f.endswith(".part") or f.endswith(".webm") or f.endswith(".m4a"):
            os.remove(f)
    for f in os.listdir("."):
        if f.endswith(".mp3"):
            return os.path.abspath(f)
