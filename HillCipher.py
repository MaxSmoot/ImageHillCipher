import numpy as np
from sympy import Matrix
import ImageManip as IManip
from PIL import Image

'''
Generate an nxn matrix that is invertible mod 256
'''


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


'''
Generate an mxn matrix that consists of 3x3 invertible mod 256 matrices
This is the key to encode the image with
'''


def generateKey(width, height, complexKey):
    key = np.empty((width, height), dtype="i")
    subkey = generateSubKey(3)
    i = 0
    j = 0
    while i < width:
        while j < height:
            if complexKey:
                subkey = generateSubKey(3)
            key[i:i+3, j:j+3] = subkey
            j += 3
        i += 3
        j = 0
    key = Image.fromarray(np.uint8(key))
    return Image.merge('RGB', (key, key, key))


'''
Convert a key to the inverse mod 256 for decrypting
'''
def invertKey(key, complexKey):
    i = 0
    j = 0
    key = np.array(key.split()[0])
    subkey = np.array(Matrix(key[i:i+3, j:j+3]).inv_mod(256))
    while i < len(key):
        while j < len(key[0]):
            if complexKey:
                subkey = np.array(Matrix(key[i:i+3, j:j+3]).inv_mod(256))
            key[i:i+3, j:j+3] = subkey
            j += 3
        i += 3
        j = 0
    key = Image.fromarray(np.uint8(key))
    return Image.merge('RGB', (key, key, key))


'''
Return a single matrix from an image of the key 
(all the color channels are the same so just extracts one of them)
'''


def extractKey(keyimage):
    return np.array(keyimage.split()[0])


'''
Encodes an image with a given key
'''
def encodeImage(key, image):
    multiplied = IManip.matrixMultImage(key, image)
    multiplied = np.array(multiplied)
    return Image.fromarray(np.uint8(np.mod(multiplied, 256)))


'''
Decodes an image with a given key
'''
def decodeImage(key, image, complexKey):
    return encodeImage(invertKey(key, complexKey), image)
