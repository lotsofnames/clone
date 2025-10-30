import yt_dlp
from ytmusicapi import YTMusic
import json
play_list_id="PLYDJHBRAlwIZd1LVEVzgIyIgOJofkigyt"
dir="C:\\Users\\matus\\Downloads\\%(title)s.%(ext)s"
yt = YTMusic()
playlist=yt.get_playlist(play_list_id)
URLS = []
#print(json.dumps(playlist, indent=4))
for i in playlist['tracks']:
    print("https://music.youtube.com/watch?v="+i['videoId'])
    URLS.append("https://music.youtube.com/watch?v="+i['videoId'])
#print(URLS)

ydl_opts = {
    'format': 'm4a/bestaudio/best',
    'outtmpl': dir ,
        'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'm4a',
    }]
}

with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    error_code = ydl.download(URLS)
