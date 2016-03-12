from PIL import Image
import matplotlib.pyplot as plt
import numpy as np

colors = {"sky": [150, 177, 224], "water": [74, 94, 228], "sand": [219, 212, 157], "grass": [
    72, 116, 55], "tree": [27, 35, 20], 'wood': [76, 60, 35], "whitewood": [173, 173, 130], "snow": [250, 250, 250]}
tolerance = {"sky": 100, "water": 100, "sand": 50, "grass": 50,
             "tree": 50, 'wood': 100, "whitewood": 60, "snow": 30}


def amount_in_array(name, array):
    return np.sum(np.sum(np.abs(array - colors[name]), axis=2) < tolerance[name]) / array.size * 3


def get_counts(array):
    gotem = 0
    for name, color in colors.items():
        amount = amount_in_array(name, array)
        print(name, amount)
        gotem += amount
    print("Got:", gotem)


def show(array, name):
    plt.imshow(np.sum(np.abs(arr2b - colors[name]), axis=2) < tolerance[name])
    plt.show()

def where_is(name, array):
    ar_left = amount_in_array(name, array[:, :array.shape[1] // 3])
    ar_middle = amount_in_array(
        name, array[:, array.shape[1] // 3:2 * array.shape[1] // 3])
    ar_right = amount_in_array(name, array[:, 2 * array.shape[1] // 3:])
    ar_top = amount_in_array(name, array[:array.shape[0] // 3])
    ar_center = amount_in_array(
        name, array[array.shape[0] // 3:2 * array.shape[0] // 3])
    ar_bottom = amount_in_array(name, array[2 * array.shape[0] // 3:])
    h = {ar_left: "left", ar_middle: "middle", ar_right: "right"}
    v = {ar_top: "top", ar_center: "center", ar_bottom: "bottom"}
    return v[max(v)] + " " + h[max(h)]

def analyzeImage(file):
    imb = Image.open(file)
    scale = 10
    im2b = imb.resize((1360//scale,768//scale),Image.LANCZOS)
    arr2b = np.array(im2b)
    import time
    t = time.time()
    get_counts(arr2b)
    for color in colors:
        print(color, ":",where_is(color,arr2b))
    print(time.time()-t)
