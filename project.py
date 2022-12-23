from tkinter import *
from tkinter import filedialog
from pytube import YouTube
import shutil


screen = Tk()
screen.title("Youtube downloader")
screen.state("zoomed")

#functions

def select_path():
    path = filedialog.askdirectory()
    path_label.config(text=path)


def download_mp4():
    #get user link
    get_link = link_field.get()
    #get selected path
    user_path = path_label.cget("text")
    #check for valid link
    try:
        mp4_video = YouTube(get_link).streams.get_highest_resolution()
    except:
        error_label=Label(screen, text = "Url Invalid")
        canvas.create_window(250,250 ,window = error_label)
        raise TypeError
    #download mp4
    mp4 = mp4_video.download()
    shutil.move(mp4,user_path)
    screen.title("download complete! Download Another file....")


def download_mp3():
    #get user link
    get_link = link_field.get()
    #get selected path
    user_path = path_label.cget("text")
    #check for valid link
    try:
        mp3_audio = YouTube(get_link).streams.filter( only_audio = True).first()
    except:
        error_label = Label(screen, text = "Url Invalid")
        canvas.create_window(250,250 ,window = error_label)
        raise TypeError
    #download mp3
    mp3 = mp3_audio.download()
    shutil.move(mp3,user_path)
    screen.title("download complete! Download Another file....")
    
    
canvas = Canvas(screen, width = 500, height = 500) 
canvas.pack()

#image logo
Logo_image = PhotoImage(file = "img\youtube.jpg")
#resize image
Logo_image = Logo_image.subsample(3,3)
canvas.create_image("250","80",image = Logo_image)

#link field
link_field = Entry(screen,width = 50)
link_label = Label(screen,text= "Insert download link here ")

#select download path
path_label =Label(screen, text = "Select Download Path")
select_button = Button(screen, text= "Select", command= select_path)

#add to windows
canvas.create_window(250,280, window= path_label)
canvas.create_window(250,330, window= select_button)

#add widgets to window
canvas.create_window(250,170, window = link_label)
canvas.create_window(250,220,window= link_field)

#add mp4_button
mp4_button = Button(screen, text = "Download mp4 format", command = download_mp4)
canvas.create_window(250,440 ,window = mp4_button)

#add mp3_button
mp3_button = Button(screen,text = "Download mp3 format", command = download_mp3)
canvas.create_window(250,490 ,window = mp3_button)







screen.mainloop()
