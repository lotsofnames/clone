import re
import yt_dlp
from ytmusicapi import YTMusic
import dearpygui.dearpygui as dpg
from tkinter import Tk, filedialog
rre=None
def button_callback(y):
    r = (dpg.get_value(y))
    if rr := re.search(r"=(.+)$", r):
        global rre
        rre=rr.group(1)
        #print(rre)
    else:
        print("No match")
def file_callback():
    global folder
    folder = filedialog.askdirectory(
        title="Vyber priečinok"
    )
   #print(folder)
dpg.create_context()
dpg.create_viewport(title='Custom Title', width=600, height=300)
with dpg.window(label="Enter playlist url", width=600, height=300):
    y=dpg.add_input_text(label="playlist url", default_value="playlist url")
    dpg.add_button(label="save location",callback=lambda:file_callback())
    dpg.add_button(label="Save",callback=lambda:button_callback(y))

dpg.setup_dearpygui()
dpg.show_viewport()
dpg.start_dearpygui()

dpg.destroy_context()
title_set = set()
#print(rre)
play_list_id = rre

titles = []
main = folder + "/"
#print(main)
#input("Press Enter to continue...")
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
    print(i["title"])
    titles.append(i["title"])
    URLS.append("https://music.youtube.com/watch?v=" + i["videoId"])
    c = c + 1
'''
print(c)
input("Press Enter to continue...")
# print(URLS)
'''
for title, url in zip(titles, URLS):
    max_pokusov = 3
    pokus = 0
    while pokus < max_pokusov:
        num = 0
        while 1:
            if title in title_set:
                title = f"{title}({num})"
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
