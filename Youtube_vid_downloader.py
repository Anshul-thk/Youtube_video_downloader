from tkinter import *
from pytube import YouTube

window=Tk()  
window.geometry("600x700")
window.config(bg="red")
window.title("Youtube Video Downloader")

Youtube_logo=PhotoImage(file="Youtube.png.png")
window.iconphoto(False,Youtube_logo)

Label(window,text="Youtube Video Downloader",font=("Arial",25,"bold"),bg="Lightgreen").pack(padx=5, pady=50)

video_link= StringVar()

Label(window, text="Enter the link : ",font=("Arial",25,"bold")).place(x=170,y=150)
Entry_link= Entry(window, width=50, font=35 ,textvariable=video_link,bd=5).place(x=35,y=200)

def video_download():
    video_url=YouTube(str(video_link.get()))
    videos= video_url.streams.first()
    videos=video_url.streams.get_highest_resolution()
    videos.download()

    Label(window, text="Download Complete",font=("Arial",20,"bold"),bg="Lightpink",fg="black").place(x=120,y=150)
    Label(window,text="Check the respective folder",font=("Arial",25,"bold"),bg="yellow",fg="black").place(x=120,y=150)

Button(window,text="Download",font=("Arial",25,"bold"),bg="white",command=video_download).place(x=180,y=300)

window.mainloop()