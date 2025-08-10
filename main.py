import yt_dlp
import argparse
from downloader import download_audio
from normalizer import normalize_audio
from file_manager import move_to_folder
from config import DEFAULT_OUTPUT_FOLDER


def extract_playlist_urls(playlist_url):
    ydl_opts = {
        "extract_flat": True,
        "quiet": True,
        "skip_download": True,
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(playlist_url, download=False)
        if "entries" in info:
            return [entry["url"] for entry in info["entries"]]
        else:
            return []


def main():
    parser = argparse.ArgumentParser(
        description="Download and normalize audio from YouTube or SoundCloud."
    )
    parser.add_argument("url", nargs="*", help="YouTube or SoundCloud URL(s)")
    parser.add_argument(
        "--output",
        "-o",
        help="Output folder path (default: configured in config.py)",
    )
    parser.add_argument(
        "--batch",
        "-b",
        help="Path to a text file containing URLs (one per line)",
    )
    parser.add_argument(
        "--playlist",
        "-p",
        help="YouTube or SoundCloud playlist URL",
    )
    args = parser.parse_args()

    output_folder = args.output if args.output else DEFAULT_OUTPUT_FOLDER

    urls = []
    if args.batch:
        try:
            with open(args.batch, "r", encoding="utf-8") as f:
                batch_urls = [line.strip() for line in f if line.strip()]
            urls.extend(batch_urls)
        except OSError as e:
            print(f"Error reading batch file: {e}")
            return
    if args.url:
        urls.extend(args.url)
    if args.playlist:
        playlist_urls = extract_playlist_urls(args.playlist)
        urls.extend(playlist_urls)
    if not urls:
        print(
            "Error: Please provide at least one URL, batch file, or playlist."
        )
        return

    for url in urls:
        print(f"Downloading audio from {url}...")
        downloaded_path = download_audio(url)

        print("Normalizing volume...")
        normalized_path = normalize_audio(downloaded_path)

        print(f"Moving file to {output_folder}...")
        move_to_folder(normalized_path, output_folder)


if __name__ == "__main__":
    main()
