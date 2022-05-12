#import tkinter module
from tkinter import *

# import system time
from time import strftime

#tkinter window
window = Tk()
window.title('Clock')

#def of the time
def time():
    string = strftime('%H:%M:%S %p')
    lbl.config(text = string)
    lbl.after(1000, time)

#styling the clock
lbl = Label(window, font = ('kabel', 40, 'bold'),
            background = 'aqua',
            foreground = 'black')
lbl.pack(anchor = 'center')

#calling the def time and the window
time()
mainloop()



