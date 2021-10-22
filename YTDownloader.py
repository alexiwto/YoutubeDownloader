import tkinter
from typing import Sized
from pytube import YouTube
from tkinter import *
from tkinter import filedialog
from tkinter import ttk


def get_streams():
    video_link = video_link_entry.get()
    if video_link != "":
        yt = YouTube(video_link)
        print("Title: " + yt.title)
        return yt.streams
    else:
        print("Video link needed")


def print_streams(streams):
    contador = 1
    for stream in streams:
        print("Stream " + str(contador) + ": " + str(stream))
        contador += 1


def download_stream():
    streams = get_streams()
    if streams is not None:
        video = (
            streams.filter(file_extension="mp4", type="video", progressive=True)
            .order_by("resolution")
            .desc()
            .first()
        )
        download_folder = download_folder_entry.get()
        if download_folder != "":
            video.download(download_folder)
            print("Video downloaded!")
        else:
            print("Download folder needed")


def set_download_folder():
    download_folder = filedialog.askdirectory()
    download_folder_entry.insert(0, download_folder)


def configure_gui(gui):
    # Window not resizable
    gui.resizable(height=False, width=False)
    # Set elements position
    video_link_label.place(x=40, y=40)
    video_link_entry.place(x=120, y=40)
    download_folder_entry.place(x=120, y=80)
    download_folder_button.place(x=440, y=80)
    download_folder_label.place(x=20, y=80)
    download_video_button.place(x=240, y=160)


gui = tkinter.Tk()
gui.title("Youtube Downloader Lite")
gui.geometry("600x480")


video_link_entry = Entry(gui, width=50)
download_folder_entry = Entry(gui, width=50)
video_link_label = Label(gui, text="Youtube URL")
download_folder_label = Label(gui, text="Download Folder")
download_folder_button = Button(gui, text="Browse", command=set_download_folder)
download_video_button = Button(gui, text="Download", command=download_stream)

configure_gui(gui)


gui.mainloop()
