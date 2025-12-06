import yt_dlp
from ytmusicapi import YTMusic


title_set = set()
play_list_id = "PLYDJHBRAlwIY_AmHgSHv7xL-2lZID-EAV"

titles = []
main = "\\\\192.168.100.7\\matus\\Pain\\"
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
play_list = {"title": titles, "URLS": URLS}
for title, url in play_list.items():
    max_pokusov = 3
    pokus = 0
    while pokus < max_pokusov:
        num = 0
        while 1:
            if title in title_set:
                title = f"{title}{num}"
                num += 1
            if title not in title_set:
                title_set.add(title)
                num = 0
                break
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
        try:
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                ydl.download([url])
            break
        except yt_dlp.utils.DownloadError as e:
            pokus += 1

        if pokus >= max_pokusov:
            break
