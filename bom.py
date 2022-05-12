import tkinter as tk
import time
window = tk.Tk()
color = ['blue', 'green', 'purple', 'black', 'red','pink']
size = ['50x50', '100x100', '150x150', '200x200', '250x250','300x300']
name = 6
for i in range(len(color)):
    window.config(bg = color[i])
    window.geometry(size[i])
    time.sleep(1)
    window.update()
    name = name - 1
    print(name)    
window.destroy
print('boom')

window.mainloop()