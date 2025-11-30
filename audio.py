import yt_dlp
from streamlit import title
from ytmusicapi import YTMusic
import json

num = 0
title_list = []
play_list_id = "PLYDJHBRAlwIZudV3Bg2eg8jNPtw8KYnRh"
titles = []
main = "\\\\192.168.100.7\\matus\\Obľúbená-hudba\\"
yt = YTMusic()
playlist = yt.get_playlist(play_list_id, limit=None)
URLS = []
# print(json.dumps(playlist, indent=4))

# for i in playlist['tracks']:

# print(i['artists'][0]['name'])
# print(i['thumbnails'])

c = 0
for i in playlist["tracks"]:
    print("https://music.youtube.com/watch?v=" + i["videoId"])
    print(i["title"] + ".%(ext)s")
    titles.append(i["title"])
    URLS.append("https://music.youtube.com/watch?v=" + i["videoId"])
    c = c + 1

print(c)
input("Press Enter to continue...")
# print(URLS)

for url, title in zip(URLS, titles):
    max_pokusov = 3
    pokus = 0
    while pokus < max_pokusov:
        if title in title_list:
            title = f"{title}{num}"
            num += 1
        ydl_opts = {
            "format": "m4a/bestaudio/best",
            "outtmpl": f"{main}{title}.%(ext)s",
            "postprocessors": [
                {
                    "key": "FFmpegExtractAudio",
                    "preferredcodec": "m4a",
                },
                {"key": "FFmpegMetadata"},
                {
                    "key": "EmbedThumbnail",  # pridanie plagátu/thumbnailu
                    "already_have_thumbnail": False,
                },
            ],
            "writethumbnail": True,
        }
        title_list.append(title)
        try:
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                ydl.download([url])
            break
        except yt_dlp.utils.DownloadError as e:
            pokus += 1

        if pokus >= max_pokusov:
            break
