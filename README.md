# yt2spot

Download and normalize audio from YouTube or SoundCloud for use as Spotify local files.

## Features
- Download audio from YouTube or SoundCloud links.
- Normalize audio for consistent volume.
- Move processed files to a specified output directory.
- Batch download support via a text file of URLs.
- Download multiple URLs directly from the command line.
- Download all tracks from a YouTube or SoundCloud playlist.

## Requirements
- Python 3.10+
- See `requirements.txt` for dependencies.

## Installation
1. Clone the repository:
   ```sh
   git clone https://github.com/stevenxngo/yt2spot.git
   cd yt2spot
   ```
2. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```

## Usage

### Single URL
```sh
python main.py "https://youtube.com/your_video_link"
```

### Multiple URLs (Command Line)
```sh
python main.py "url1" "url2" "url3"
```

### Batch Download (Text File)
Create a text file (e.g., `urls.txt`) with one URL per line:
```
https://youtube.com/first_video
https://soundcloud.com/second_track
```
Run:
```sh
python main.py --batch urls.txt
```
or
```sh
python main.py -b urls.txt
```

### Playlist Download
Download all tracks from a playlist:
```sh
python main.py --playlist "playlist_url_here"
```
or
```sh
python main.py -p "playlist_url_here"
```

### Combine Command Line URLs, Batch File, and Playlist
```sh
python main.py "url1" "url2" --batch urls.txt --playlist "playlist_url_here"
```
All URLs will be processed.

### Output Directory
Specify a custom output folder:
```sh
python main.py "url1" "url2" --output /path/to/folder
```
If not specified, the default output folder is set in `config.py`.

## License
See `LICENSE` for details.