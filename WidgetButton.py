import tkinter as tk
import random
window = tk.Tk()
RandomLijst = ['Powerbank','Laptop','Phone','Headphone','Bag','Charger','Shoes']
def RandomGrab():
    if(button['text']=='Grab!'):
        b = random.choice(RandomLijst)
        button['text']='Grabbed!'
        print(b)
        RandomLijst.remove(b)
    else:
        print(RandomLijst)
        button['text']=('Grab!')

window['background']='teal'
button = tk.Button(text='Grab!', foreground='black', command=RandomGrab)
button.pack(pady = 20, padx = 20)
window.mainloop()
