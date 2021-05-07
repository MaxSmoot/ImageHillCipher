from PIL import Image
import numpy as np
from sympy import Matrix


'''
Convert an image to a padded image whose dimensions are both divisible by 3
'''
def padImage(image_pixels, padnum):
    hlength = len(image_pixels)
    vlength = len(image_pixels[0])
    if(hlength % padnum != 0):
        buffer_col = np.full((1, vlength, 3), 0, dtype="uint8")
        for _ in range(0, padnum - (hlength % padnum)):
            image_pixels = np.vstack((image_pixels, buffer_col))
            hlength += 1
    if(vlength % padnum != 0):
        buffer_row = np.full((hlength, 1, 3), 0, dtype="uint8")
        for _ in range(0, padnum - (vlength % padnum)):
            image_pixels = np.hstack((image_pixels, buffer_row))
            vlength += 1
    return Image.fromarray(image_pixels)


'''
Left Multiply 3x3 chunks of the image by corresponding 3x3 chunks of the key
Multiplies all the color channels by the key then combines to a single matrix
'''
def matrixMultImage(key, image, block_size):
    colorChannels = image.split()
    encryptedChannels = []
    key = np.array(key.split()[0])
    i = 0
    j = 0
    for colorChannel in colorChannels:
        singleChannel = np.array(colorChannel)
        while(i < len(singleChannel)):
            while(j < len(singleChannel[0])):
                singleChannel[i:i+block_size, j:j+block_size] = np.matmul(key[i:i+block_size, j:j+block_size], singleChannel[i:i+block_size, j:j+block_size])
                j += block_size
            i += block_size
            j = 0
        i = 0
        encryptedChannels.append(Image.fromarray(singleChannel))
    return Image.merge('RGB', encryptedChannels)
