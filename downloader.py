import yt_dlp

def download_video(url, output_path="downloads"):
    ydl_opts = {
        "outtmpl": f"{output_path}/%(title)s.%(ext)s",
        "format": "best"
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])
