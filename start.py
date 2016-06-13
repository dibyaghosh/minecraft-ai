import win32con
from win32api import keybd_event, mouse_event
import time
import random
import win32api

def move_forward(t):
    a = time.time()
    while time.time()-a < t:
        Key = Base['w']
        KeyDown(Key)
        time.sleep(.05)
    KeyUp(Key)

def move_back(t):
    a = time.time()
    while time.time()-a < t:
        Key = Base['s']
        KeyDown(Key)
        time.sleep(.05)
    KeyUp(Key)

def move_left(t):
    a = time.time()
    while time.time()-a < t:
        Key = Base['a']
        KeyDown(Key)
        time.sleep(.1)
    KeyUp(Key)

def move_right(t):
    a = time.time()
    while time.time()-a < t:
        Key = Base['d']
        KeyDown(Key)
        time.sleep(.1)
    KeyUp(Key)

def get_inventory():
    Key = Base['e']
    KeyDown(Key)
    time.sleep(.1)
    KeyUp(Key)

def leave_inventory():
    Key = Base['ESC']
    KeyDown(Key)
    time.sleep(.1)
    KeyUp(Key)

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


def click(t):
    mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)
    time.sleep(t)
    mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0, 0, 0)

def rotate(degrees):
    """
    Assuming 1366*768 resolution
    Cursor speed (right): (730,384)
Full revolution time: ~1.65 sec

Cursor speed (left): (636,384)
Full revolution time: ~1.65 sec
    """
    degrees%=360
    if(degrees > 180):
        win32api.SetCursorPos()
        loc = (730,384)
        degrees = 360 - degrees
    else:
        loc = (636,384)
    a = time.time()
    print(degrees/360*1.65)
    while time.time()-a < degrees/360*1.65:
        win32api.SetCursorPos(loc)
        time.sleep(.03)

def v_rotate(degrees):
    """
    Assuming 1366*768 resolution
    Cursor speed (right): (730,384)
Full revolution time: ~1.65 sec

Cursor speed (left): (636,384)
Full revolution time: ~1.65 sec
    """
    degrees%=360
    if(degrees > 180):
        win32api.SetCursorPos()
        loc = (683,410)
        degrees = 360 - degrees
    else:
        loc = (683,358)
    a = time.time()
    print(degrees/360*1.65)
    while time.time()-a < degrees/360*1.65:
        win32api.SetCursorPos(loc)
        time.sleep(.03)

def center():
    win32api.SetCursorPos([683,375])
