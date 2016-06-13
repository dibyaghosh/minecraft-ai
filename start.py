import win32con
from win32api import keybd_event, mouse_event
import time
import random
import win32api

from PIL import ImageGrab
from image import *
from MCKeyboard import *



def try_get():
    print("Move into Minecraft")
    time.sleep(5)
    MCK = MC_Window()
    MCK.move_forward(1)

def new_main():
    print("Move into Minecraft")
    time.sleep(4)
    im = ImageGrab.grab()
    arr = analyzeImage(im)
    while amount_in_array("wood",arr) > .01:
        im = ImageGrab.grab()
        arr = analyzeImage(im)
        hor,ver = where_is("wood",arr)
        if hor == "middle" and ver =="center":
            break
        if hor == "left":
            rotate(45)
        elif hor == "right":
            rotate(-45)
        elif ver == "top":
            v_rotate(45)
        elif ver == "bottom":
            v_rotate(-45)

def main():
    print("Move into Minecraft")
    time.sleep(2)
    images = []
    MCK = MC_Window()
    try:
        while True:
            im = ImageGrab.grab()
            images.append(im)
            analyzeImage(im)
            MCK.move_forward(1)
            im = ImageGrab.grab()
            analyzeImage(im)
            images.append(im)
            MCK.move_left(1)
            im = ImageGrab.grab()
            analyzeImage(im)
            images.append(im)
            MCK.move_back(1)
            im = ImageGrab.grab()
            analyzeImage(im)
            images.append(im)
            MCK.move_right(1)
            im = ImageGrab.grab()
            analyzeImage(im)
            images.append(im)
            time.sleep(1)
            MCK.mine(1)
            MCK.rotate(170)
            MCK.get_inventory()
            time.sleep(1)
            MCK.leave_inventory()
    except Exception as e:
        print(e,"Got exception!")
        return images
    return images
