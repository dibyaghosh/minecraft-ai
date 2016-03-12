from tkinter import *
from PIL import Image, ImageTk
from sectionify import sectionify
import numpy as np
from block_svc import *

#f = Image.open("file URL")



root = Tk()
root.geometry('1000x1000')
w = Entry(root)
w.pack()
canvas = Canvas(root,width=999,height=999)
canvas.pack()
pilImage = Image.open("pic.jpg")

sections = sectionify(5, np.array(pilImage))

image = ImageTk.PhotoImage(Image.fromarray(sections[0]))
imagesprite = canvas.create_image(400,400,image=image)

i = 0

n = NewSVC()

def enter(e):
    global i
    global imagesprite
    s = w.get()
    n.add_prediction(np.array(sections[i]), s)

    i += 1

    image = ImageTk.PhotoImage(Image.fromarray(sections[i]))
    print(n.guess(sections[i]))
    canvas.delete(imagesprite)

    imagesprite = canvas.create_image(400,400,image=image)
    error()


w.bind("<Return>", enter)

root.mainloop()
