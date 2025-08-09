import subprocess
import os


def normalize_audio(input_path):
    temp_path = os.path.splitext(input_path)[0] + "_temp.mp3"
    subprocess.run(
        [
            "ffmpeg",
            "-y",
            "-i",
            input_path,
            "-af",
            "loudnorm=I=-14:TP=-1.0:LRA=11",
            temp_path,
        ],
        check=True,
    )
    os.replace(temp_path, input_path)
    return os.path.abspath(input_path)
