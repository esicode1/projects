#!/usr/bin/env python3

__author__ = 'ehsangb180@gmail.com'

from tkinter import*
import string
import random

root = Tk()
root.geometry("400x400+0+0")
root.title("Code Generator")

lblInfo = Label(root, font=("arial", 20, "bold"), text="Code Generator", fg="goldenrod1", bd=10, anchor='w')
lblInfo.grid(row=0, column=1)

def ref():
    total = string.printable
    length = 16
    password = "".join(random.sample(total, length))
    rand.set(password)
    
def exit():
    root.destroy()

def reset():
    rand.set("")

rand = StringVar()

lblReference = Label(root, font=("arial", 10, "bold"), text="password", bd=16, anchor="w")
lblReference.grid(row=2, column=0)
txtReference = Entry(root, font=("arial", 10, "bold"), textvariable=rand, bd=10, insertwidth=4,
                     bg="steelblue2", justify="right")
txtReference.grid(row=2, column=1)
btnTotal = Button(root, padx=8, pady=8, bd=8, fg="black", font=("arial", 10), width=4,
                  text="Generate", bg="goldenrod1", command=lambda: ref()).grid(row=9, column=0)
btnReset = Button(root, padx=8, pady=8, bd=8, fg="black", font=("arial", 10), width=4,
                  text="Reset", bg="goldenrod1", command=lambda: reset()).grid(row=9, column=1)
btnExit = Button(root, padx=8, pady=8, bd=8, fg="black", font=("arial", 10), width=4,
                  text="Exit", bg="red2", command=lambda: exit()).grid(row=9, column=2)

root.mainloop()
