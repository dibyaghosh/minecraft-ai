import win32con
from win32api import keybd_event, mouse_event
import time
import random
import win32api


Combs = {
    'A': [
        'SHIFT',
        'a'],
    'B': [
        'SHIFT',
        'b'],
    'C': [
        'SHIFT',
        'c'],
    'D': [
        'SHIFT',
        'd'],
    'E': [
        'SHIFT',
        'e'],
    'F': [
        'SHIFT',
        'f'],
    'G': [
        'SHIFT',
        'g'],
    'H': [
        'SHIFT',
        'h'],
    'I': [
        'SHIFT',
        'i'],
    'J': [
        'SHIFT',
        'j'],
    'K': [
        'SHIFT',
        'k'],
    'L': [
        'SHIFT',
        'l'],
    'M': [
        'SHIFT',
        'm'],
    'N': [
        'SHIFT',
        'n'],
    'O': [
        'SHIFT',
        'o'],
    'P': [
        'SHIFT',
        'p'],
    'R': [
        'SHIFT',
        'r'],
    'S': [
        'SHIFT',
        's'],
    'T': [
        'SHIFT',
        't'],
    'U': [
        'SHIFT',
        'u'],
    'W': [
        'SHIFT',
        'w'],
    'X': [
        'SHIFT',
        'x'],
    'Y': [
        'SHIFT',
        'y'],
    'Z': [
        'SHIFT',
        'z'],
    'V': [
        'SHIFT',
        'v'],
    'Q': [
        'SHIFT',
        'q'],
    '?': [
        'SHIFT',
        '/'],
    '>': [
        'SHIFT',
        '.'],
    '<': [
        'SHIFT',
        ','],
    '"': [
        'SHIFT',
        "'"],
    ':': [
        'SHIFT',
        ';'],
    '|': [
        'SHIFT',
        '\\'],
    '}': [
        'SHIFT',
        ']'],
    '{': [
        'SHIFT',
        '['],
    '+': [
        'SHIFT',
        '='],
    '_': [
        'SHIFT',
        '-'],
    '!': [
        'SHIFT',
        '1'],
    '@': [
        'SHIFT',
        '2'],
    '#': [
        'SHIFT',
        '3'],
    '$': [
        'SHIFT',
        '4'],
    '%': [
        'SHIFT',
        '5'],
    '^': [
        'SHIFT',
        '6'],
    '&': [
        'SHIFT',
        '7'],
    '*': [
        'SHIFT',
        '8'],
    '(': [
        'SHIFT',
        '9'],
    ')': [
        'SHIFT',
        '0'] }
Base = {
    '0': 48,
    '1': 49,
    '2': 50,
    '3': 51,
    '4': 52,
    '5': 53,
    '6': 54,
    '7': 55,
    '8': 56,
    '9': 57,
    'a': 65,
    'b': 66,
    'c': 67,
    'd': 68,
    'e': 69,
    'f': 70,
    'g': 71,
    'h': 72,
    'i': 73,
    'j': 74,
    'k': 75,
    'l': 76,
    'm': 77,
    'n': 78,
    'o': 79,
    'p': 80,
    'q': 81,
    'r': 82,
    's': 83,
    't': 84,
    'u': 85,
    'v': 86,
    'w': 87,
    'x': 88,
    'y': 89,
    'z': 90,
    '.': 190,
    '-': 189,
    ',': 188,
    '=': 187,
    '/': 191,
    ';': 186,
    '[': 219,
    ']': 221,
    '\\': 220,
    "'": 222,
    'ALT': 18,
    'TAB': 9,
    'CAPSLOCK': 20,
    'ENTER': 13,
    'BS': 8,
    'CTRL': 17,
    'ESC': 27,
    ' ': 32,
    'END': 35,
    'DOWN': 40,
    'LEFT': 37,
    'UP': 38,
    'RIGHT': 39,
    'SELECT': 41,
    'PRINTSCR': 44,
    'INS': 45,
    'DEL': 46,
    'LWIN': 91,
    'RWIN': 92,
    'LSHIFT': 160,
    'SHIFT': 161,
    'LCTRL': 162,
    'RCTRL': 163,
    'VOLUP': 175,
    'DOLDOWN': 174,
    'NUMLOCK': 144,
    'SCROLL': 145 }

def KeyUp(Key):
    keybd_event(Key, 0, 2, 0)


def KeyDown(Key):
    keybd_event(Key, 0, 1, 0)


def Press(Key, speed=1):
    rest_time = 0.05/speed
    if Key in Base:
        Key = Base[Key]
        KeyDown(Key)
        time.sleep(rest_time)
        KeyUp(Key)
        return True
    if Key in Combs:
        KeyDown(Base[Combs[Key][0]])
        time.sleep(rest_time)
        KeyDown(Base[Combs[Key][1]])
        time.sleep(rest_time)
        KeyUp(Base[Combs[Key][1]])
        time.sleep(rest_time)
        KeyUp(Base[Combs[Key][0]])
        return True
    return False

def Write(Str, speed = 1):
    for s in Str:
        Press(s, speed)
        time.sleep((0.1 + random.random()/10.0) / float(speed))

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
