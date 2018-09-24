import tkinter
from tkinter import *

root = Tk()
#canvas = Canvas(width = 300, height = 200, bg = 'yellow')
#canvas.pack(expand = YES, fill = BOTH)
#gif1 = PhotoImage(file = 'myImage.gif')
#canvas.create_image(0, 0, image=gif1, anchor = NW)
list ='4   4   4  4   44'
item=" ".join(list)
w = Label(root, text=item)
w.pack()

root.mainloop()