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
v = StringVar()
Label(root, textvariable=v).pack()
canvas = Canvas(root,width=999,height=999)
canvas.pack()
pilImage = Image.open("/home/dibya/Downloads/d.jpg")

n = NewSVC.load_from_file("blockdata")
sections = sectionify(10, np.array(pilImage))
#sections = sections[len(n.y):]

image = ImageTk.PhotoImage(Image.fromarray(sections[0]).resize((400,400)))
imagesprite = canvas.create_image(400,400,image=image)

i = 0


def enter(e):
    global i
    global imagesprite
    s = w.get()
    n.add_prediction(np.array(sections[i]), s)

    i += 1

    image = ImageTk.PhotoImage(Image.fromarray(sections[i]).resize((400,400)))
    v.set("Guessing "+str(n.guess(sections[i])))
    print("Guessing",n.guess(sections[i]))
    canvas.delete(imagesprite)

    imagesprite = canvas.create_image(400,400,image=image)
    error()

w.bind("<Return>", enter)

root.mainloop()
