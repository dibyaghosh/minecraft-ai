import win32con
from win32api import keybd_event, mouse_event
import time
import random
import win32api


from PIL import ImageGrab
from image import *

def try_get():
    print("Move into Minecraft")
    time.sleep(5)
    im = ImageGrab.grab()
    analyzeImage(im)
    return im

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
    try:
        while True:
            im = ImageGrab.grab()
            images.append(im)
            analyzeImage(im)
            move_forward(1)
            im = ImageGrab.grab()
            analyzeImage(im)
            images.append(im)
            move_left(1)
            im = ImageGrab.grab()
            analyzeImage(im)
            images.append(im)
            move_back(1)
            im = ImageGrab.grab()
            analyzeImage(im)
            images.append(im)
            move_right(1)
            im = ImageGrab.grab()
            analyzeImage(im)
            images.append(im)
            time.sleep(1)
            click(1)
            rotate(170)
            get_inventory()
            time.sleep(1)
            leave_inventory()
    except:
        return images
    return images
