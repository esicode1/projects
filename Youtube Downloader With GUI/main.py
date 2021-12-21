#!/usr/bin/env python3

__author__ = "ehsangb180@gmail.com"

'''
    1. make a virtualenv and activate it.
    2. if necessary, connect to a stable VPN.
    3. give your youtube URL and download it. 

'''
import os
from tkinter.font import BOLD
from pytube import *
from tkinter import *
from tkinter.filedialog import *
from tkinter.messagebox import *
from threading import *
file_size = 0


def progress(stream=None, chunk=None,  remaining=None):
    file_downloaded = (file_size-remaining)
    per = round((file_downloaded/file_size)*100, 1)
    dBtn.config(text=f'{per}% downloaded')

def startDownload():
    global file_size
    try:
        URL = urlField.get()
        dBtn.config(text='Please wait...')
        dBtn.config(state=DISABLED)
        path_save = askdirectory()
        if path_save is None:
            return
        
        ob = YouTube(URL, on_progress_callback=progress)
        print(ob)
        strm = ob.streams[0]
        print(strm)
        x = ob.description.split("|")
        print(x)
        
        file_size = strm.filesize
        dfile_size = file_size
        dfile_size /= 1000000
        dfile_size = round(dfile_size, 2)
        label.config(text='Size: ' + str(dfile_size) + ' MB')
        label.pack(side=TOP, pady=10)
        desc.config(text=ob.title + '\n\n' + 'Label: ' + ob.author + '\n\n' + 'length: ' + str(round(ob.length/60, 1)) + ' mins\n\n'
                    'Views: ' + str(round(ob.views/1000000, 2)) + 'M')
        desc.pack(side=TOP, pady=10)
        strm.download(path_save, strm.title)
        dBtn.config(state=NORMAL)
        showinfo("Download Finished", 'Downloaded Successfully')
        urlField.delete(0, END)
        label.pack_forget()
        desc.pack_forget()
        dBtn.config(text='Start Download')

    except Exception as e:
        # print(e)
        # print('Error!!')
        pass

def startDownloadthread():
    thread = Thread(target=startDownload)
    thread.start()

    
main = Tk()
main.title("YouTube Downloader")
main.config(bg='#e6000a')
main.geometry("300x400")

file = PhotoImage(file='./photo.png')
headingIcon = Label(main, image=file)
headingIcon.pack(side=TOP)

urlField = Entry(main, font=("Times New Roman", 12), justify=CENTER)
urlField.pack(side=TOP, fill=X, padx=10, pady=15)

dBtn = Button(main, text="Start Download", font=(
    "Times New Roman", 14), relief='ridge', activeforeground='red',
    command=startDownloadthread)
dBtn.pack(side=TOP)

exitBtn = Button(main, text="Exit", font=(
    "Times New Roman", 14), relief='ridge', activeforeground='red',
    command=main.destroy)
exitBtn.pack(side=TOP)

label = Label(main, text='')
desc = Label(main, text='')
author = Label(main, text="ehsangb180@gmail.com")
author.config(bg='#e6000a',font=("Courier", 10,BOLD))
author.pack(side=BOTTOM)
main.mainloop()
