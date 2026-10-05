import yt_dlp

url = input("Enter YouTube URL: ")

options = {
    "format": "bestaudio/best",
    "outtmpl": "%(title)s.%(ext)s",
    "postprocessors": [
        {
            "key": "FFmpegExtractAudio",
            "preferredcodec": "mp3",
            "preferredquality": "192",
        }
    ],
}

try:
    with yt_dlp.YoutubeDL(options) as ydl:
        ydl.download([url])

    print("Done! MP3 saved successfully.")

except Exception as e:
    print(f"Error: {e}")