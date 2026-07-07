from yt_dlp import YoutubeDL
import json

ytdl_format_options = {
    "format": "bestaudio/best",
    "noplaylist": True,
    "quiet": True,
    "extract_flat": False,
}

ytdl = YoutubeDL(ytdl_format_options)

info = ytdl.extract_info("https://www.youtube.com/watch?v=81dezsUC3nc&list=RDMM&start_radio=1&rv=BcqPl8A9cM0", download=False)

with open("info.txt", "w", encoding="utf-8") as f:
    json.dump(info, f, indent=4, ensure_ascii=False)