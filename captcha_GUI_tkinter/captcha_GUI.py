#!/usr/bin/env python3

__author__ = 'ehsangb180@gmail.com'

import  random
import string
from tkinter import Tk, Label, Entry, Button, END
from PIL import ImageTk, Image
from captcha.image import ImageCaptcha

def createCaptcha(flag=0):

    global random_string
    global image_label
    global image_display
    global entry
    global verify_label

    if flag == 1:
        verify_label.grid_forget()

    entry.delete(0, END)
    random_string = ''.join(random.choices(string.ascii_letters + string.digits, k=4))
    image_captcha = ImageCaptcha(width=250, height=125)
    image_generated = image_captcha.generate(random_string)
    image_display = ImageTk.PhotoImage(Image.open(image_generated))
    image_label.grid_forget()
    image_label = Label(root, image=image_display)
    image_label.grid(row=1, column=0, columnspan=2, padx=10)

def check(x, y):

    global verify_label
    verify_label.grid_forget()

    if x.lower() == y.lower():
        verify_label = Label(master=root,text="Verified",font="Arial 15",bg='#ffe75c',fg="#00a806")
        verify_label.grid(row=0, column=0, columnspan=2, pady=10)
    else:
        verify_label = Label(master=root,text="Incorrect!",font="Arial 15",bg='#ffe75c',fg="#fa0800")
        verify_label.grid(row=0, column=0, columnspan=2, pady=10)
        createCaptcha()

if __name__ == "__main__":
    
    root = Tk()
    root.title('Captcha by esigoo')

    verify_label = Label(root)
    image_label = Label(root)
    
    entry = Entry(root, width=10, borderwidth=5,font="Arial 15", justify="center")
    entry.grid(row=2, column=0)

    createCaptcha()

    reload_img = ImageTk.PhotoImage(Image.open('reload.png').resize((32, 32), Image.ANTIALIAS))
    reload_button = Button(image=reload_img, command=lambda: createCaptcha(1))
    reload_button.grid(row=2, column=1, pady=10)

    submit_button = Button(root, text="Submit", font="Arial 10", command=lambda: check(entry.get(), random_string))
    submit_button.grid(row=3, column=0, columnspan=2, pady=10)

    exit_button = Button(root, text="Exit",font="Arial 10",command=root.destroy)
    exit_button.grid(row=3, column=1, columnspan=2,pady=10)

    root.bind('<Return>', func=lambda Event: check(entry.get(), random_string))
    root.mainloop()
