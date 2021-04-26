import numpy as np
from sympy import Matrix
from ImageManip import extractColorChannels


def generateSubKey(sub_size):
    found = False
    while(not found):
        key = np.array([[np.random.randint(256)
                       for x in range(0, sub_size)] for y in range(0, sub_size)])
        try:
            Matrix(key).inv_mod(256)
            found = True
        except:
            pass
    return key


def generateKey(width, height):
    print(width, height)
    key = np.empty((width, height), dtype="i")
    i = 0
    j = 0
    while i < width:
        while j < height:
            subkey = generateSubKey(3)
            key[i:i+3, j:j+3] = subkey
            j += 3
        i += 3
        j = 0
    return key


def invertKey(key):
    i = 0
    j = 0
    while i < len(key):
        while j < len(key[0]):
            key[i:i+3, j:j+3] = np.array(Matrix(key[i:i+3, j:j+3]).inv_mod(256))
            j+=3
        i+=3
        j = 0
    return key


def extractKey(keyimage):
    return extractColorChannels(keyimage)["red"]

