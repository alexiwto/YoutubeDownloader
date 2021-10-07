import tkinter
from pytube import YouTube
from tkinter import *
from tkinter import filedialog
from tkinter import ttk


def get_streams():
    video_link = video_link_entry.get()
    yt = YouTube(video_link)
    print("Title: " + yt.title)
    print("Getting all MP4 streams")
    set_streams_list(yt.streams)


def print_streams(streams):
    contador = 1
    for stream in streams.filter(file_extension="mp4"):
        print("Stream " + str(contador) + ": " + str(stream))
        contador += 1


def set_streams_list(streams):
    for stream in (
        streams.filter(file_extension="mp4", type="video", progressive=True)
        .order_by("resolution")
        .desc()
    ):
        stream_list.append(stream)


def set_streams_dropdown():
    if stream_list:
        stream_list_dropdown["values"] = stream_list
        print(stream_list)
        stream_list.clear()


def set_download_folder():
    download_folder = filedialog.askdirectory()
    download_folder_entry.insert(0, download_folder)
    print(download_folder)


def configure_gui(gui):
    # Window not resizable
    gui.resizable(height=False, width=False)
    # Set elements position
    video_link_label.place(x=20, y=20)
    video_link_entry.place(x=180, y=20)
    check_streams_button.place(x=500, y=20)
    download_folder_entry.place(x=180, y=60)
    download_folder_button.place(x=500, y=60)
    download_folder_label.place(x=20, y=60)
    stream_list_dropdown.place(x=20, y=120)


gui = tkinter.Tk()
gui.title("Youtube Downloader Lite")
gui.geometry("852x480")

stream_list = []
video_link_entry = Entry(gui, width=50)
download_folder_entry = Entry(gui, width=50)
video_link_label = Label(gui, text="Youtube URL")
download_folder_label = Label(gui, text="Download Folder")
check_streams_button = Button(gui, text="Check Streams", command=get_streams)
download_folder_button = Button(gui, text="Browse", command=set_download_folder)
stream_list_dropdown = ttk.Combobox(
    gui, values=stream_list, postcommand=set_streams_dropdown, width=120
)
stream_list_dropdown.set("Select a stream")


configure_gui(gui)


gui.mainloop()
