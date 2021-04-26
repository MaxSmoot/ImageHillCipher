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


def generateKey(size):
    key = np.empty((size, size), dtype="i")
    i = 0
    j = 0
    while i < size:
        while j < size:
            subkey = generateSubKey(3)
            key[i:i+3, j:j+3] = subkey
            j += 3
        i += 3
        j = 0
    return key


def invertKey(key):
    i = 0
    j = 0
    size = len(key)
    while i < size:
        while j < size:
            key[i:i+3, j:j+3] = np.array(Matrix(key[i:i+3, j:j+3]).inv_mod(256))
            j+=3
        i+=3
        j = 0
    return key


def extractKey(keyimage):
    return extractColorChannels(keyimage)["red"]

