from tkinter import *

root = Tk()
root.title('Hello')
root.geometry('300x200')

doos = Label(
    root,
    text = 'Hello Tkinker',
    bg = 'green',
    fg = 'red'
)
doos.pack(
    expand = True,
    fill = 'both',
    ipadx=10,
    ipady=10
)

root.mainloop()