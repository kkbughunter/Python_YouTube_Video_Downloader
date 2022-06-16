import tkinter as tk 
from pytube import YouTube as yt
from tkinter.font import Font
from pytube import YouTube as yt

def Show_video(): # to display the video title
    main_url = videourl.get()
    download_aim = yt(main_url)
    dis_titile = tk.Label(root,text=" Video Title : " + download_aim.title,font=("time",20))
    dis_titile.pack()
    Downbtn = tk.Button(root,text="       Download       ",bg="green2",padx=40,pady=5, height=1,command=Download_video)
    Downbtn.pack()

def Download_video(): # to download the video
    main_url = videourl.get()
    download_aim = yt(main_url)
    download_aim = download_aim.streams.get_highest_resolution()
    download_aim.download()
    titlefont = Font(family="Bradley Hand ITC",size=23) 
    title = tk.Label(root,text="--------------------------------\nDownload Completed \n Thank You\n-------------------------------- ",font=titlefont,fg="blue")
    title.pack()


root = tk.Tk()  

root.geometry("950x650")
root.title("Youtube Saver")

titlefont = Font(family="Algerian",size=23,weight= "bold") 
title = tk.Label(root,text="Welcome to KK BUG HUNTER\nYouTube Saver\n\n\n\n\n",font=titlefont)
title.pack()


text = tk.Label(root,text="Enter the URL Hear",font=titlefont)
text.pack()

videourl = tk.Entry(root,width=50,font=("time",20),border=9,bg="light blue")
videourl.pack()

Downbtn = tk.Button(root,text="See Video",bg="green2",padx=40,pady=5, height=1,command=Show_video)
Downbtn.pack()
#-----------------------------------------------------------------------------------#

root.mainloop()  