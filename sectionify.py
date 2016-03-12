import numpy as np
from PIL import Image

sections = 10
im = np.array(f)

def sectionify(n, l):
    row_length = len(l[0])
    column_length = len(l)

    length_rsections = row_length//n
    length_csections = column_length//n
    
    grouped_l = []

    for i in range(n):
        for j in range(n):
            grouped_l.append(l[i*length_rsections:(i+1)*length_rsections,j*length_csections:(j+1)*length_csections])
    return grouped_l
