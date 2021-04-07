from pytube import YouTube
import tkinter as tk
from tkinter import *

root = tk.Tk()

def youtube_app():
    te = text_entry.get()

    # YouTube("https://www.youtube.com/watch?v=xdcSFVXd3MU").streams.first().download()
    yt = YouTube(te)
    # yt.streams
    yt_info = f'{yt.title}, {yt.streams}, {yt.thumbnail_url}'
    output_textbox.insert(INSERT, yt_info)

    print(yt.title)
    print(yt.streams)
    print(yt.thumbnail_url)

    yt.streams.first().download()


text_entry = tk.Entry(width=100)
text_entry.pack()

download_button = tk.Button(text="download", command=youtube_app)
download_button.pack()

output_textbox = tk.Text()
output_textbox.pack()





root.mainloop()


