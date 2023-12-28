
#the youtube video downloader by sterckx-it 


from tkinter import Tk, Label, Entry, Button, StringVar
from pytube import YouTube
from tkinter import PhotoImage

def download_video():
    url = url_input.get()
    yt = YouTube(url)
    print("Title: ", yt.title)
    ys = yt.streams.get_highest_resolution()
    print("Downloading...")
    ys.download()
    print("Download complete")

root = Tk()
root.title("youtube downloader")  # Change the title to "sterckx-it"

Label(root, text="Enter YouTube URL:").pack()
url_input = StringVar()
Entry(root, textvariable=url_input, width=100).pack()
logo_image = PhotoImage(file="./images/logo.png")
icon_image = PhotoImage(file="./images/icon.png")
root.iconphoto(True, icon_image)  # Set the icon to the logo image
logo_image = PhotoImage(file="./images/logo.png")
logo_image = logo_image.subsample(2)  # Reduce the size by a factor of 2
logo_label = Label(root, image=logo_image)
logo_label.pack()
Button(root, text="Download", command=download_video).pack()

root.mainloop()