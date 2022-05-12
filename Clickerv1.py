from tkinter import *
window = Tk()

window.counter = 0

def clicked():
    window.counter += 1
    L['text'] = 'ButtonClicked: ' + str(window.counter)

def clickedDown():
    window.counter -= 1
    L['text'] = 'buttonClicked: ' + str(window.counter) 

b = Button(window, text="up", command=clicked)
b.pack()

c = Button(window,text= "buttonDown", command= clickedDown)
c.pack() 

L = Label(window, text="No clicks yet.")
L.pack()

window.mainloop()
