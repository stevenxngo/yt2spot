import argparse
from downloader import download_audio
from normalizer import normalize_audio
from file_manager import move_to_folder
from config import DEFAULT_OUTPUT_FOLDER


def main():
    parser = argparse.ArgumentParser(
        description="Download and normalize audio from YouTube or SoundCloud."
    )
    parser.add_argument("url", help="YouTube or SoundCloud URL")
    parser.add_argument(
        "--output",
        "-o",
        help="Output folder path (default: configured in config.py)",
    )
    args = parser.parse_args()

    output_folder = args.output if args.output else DEFAULT_OUTPUT_FOLDER

    print(f"Downloading audio from {args.url}...")
    downloaded_path = download_audio(args.url)

    print("Normalizing volume...")
    normalized_path = normalize_audio(downloaded_path)

    print(f"Moving file to {output_folder}...")
    move_to_folder(normalized_path, output_folder)


if __name__ == "__main__":
    main()
