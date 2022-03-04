import tkinter
from tkinter.constants import COMMAND
from tkinter import *

window = tkinter.Tk()
window.title("Mapricho")
window.minsize(width=500, height=300)

def login():
    print(f'Logged in succesful')

#Button
button = Button(text="Click Me", command=login)
button.pack()

#Entry
input = Entry(width=10)
input.pack()
print(input.get())

window.mainloop()