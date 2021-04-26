from PIL import Image
import numpy as np
from sympy import Matrix


'''
Convert an image to a padded image whose dimensions are both divisible by 3
'''
def padImage(image_pixels):
    hlength = len(image_pixels)
    vlength = len(image_pixels[0])
    if(hlength % 3 != 0):
        buffer_col = np.full((1, vlength, 3), 0, dtype="uint8")
        for i in range(0, 3 - (hlength % 3)):
            image_pixels = np.vstack((image_pixels, buffer_col))
            hlength += 1
    if(vlength % 3 != 0):
        buffer_row = np.full((hlength, 1, 3), 0, dtype="uint8")
        for i in range(0, 3 - (vlength % 3)):
            image_pixels = np.hstack((image_pixels, buffer_row))
            vlength += 1
    return image_pixels

'''
Convert an image matrix to a dictionary with three keys: red,blue,green 
whose values are the matrices of the color channels of the image
'''
def extractColorChannels(imagearr):
    red_channel = np.empty((len(imagearr), len(imagearr[0])), dtype="i")
    green_channel = np.empty((len(imagearr), len(imagearr[0])), dtype="i")
    blue_channel = np.empty((len(imagearr), len(imagearr[0])), dtype="i")
    for i in range(0, len(imagearr)):
        for j in range(0, len(imagearr[0])):
            red, green, blue = imagearr[i, j]
            red_channel[i, j] = red
            green_channel[i, j] = green
            blue_channel[i, j] = blue
    return {"red": red_channel, "green": green_channel, "blue": blue_channel}

'''
Convert a dictionary of color channels into a single matrix
'''
def combineColorChannels(imagearr):
    combined = np.empty((len(imagearr["red"]), len(
        imagearr["red"][0]), 3))
    for i in range(0, len(imagearr["red"])):
        for j in range(0, len(imagearr["red"][0])):
            combined[i, j] = imagearr["red"][i,
                                             j], imagearr["green"][i, j], imagearr["blue"][i, j]
    return combined

'''
Left Multiply 3x3 chunks of the image by corresponding 3x3 chunks of the key
Multiplies all the color channels by the key then combines to a single matrix
'''
def matrixMultImage(key, image):
    split_image = extractColorChannels(image)
    i = 0
    j = 0
    while(i < len(split_image["red"])):
        while(j < len(split_image["red"][0])):
            red_chunk = split_image["red"][i:i+3, j:j+3]
            red_chunk = np.matmul(key[i:i+3, j:j+3], red_chunk)
            green_chunk = split_image["green"][i:i+3, j:j+3]
            green_chunk = np.matmul(key[i:i+3, j:j+3], green_chunk)
            blue_chunk = split_image["blue"][i:i+3, j:j+3]
            blue_chunk = np.matmul(key[i:i+3, j:j+3], blue_chunk)
            split_image["red"][i:i+3, j:j+3] = red_chunk
            split_image["green"][i:i+3, j:j+3] = green_chunk
            split_image["blue"][i:i+3, j:j+3] = blue_chunk
            j += 3
        i += 3
        j = 0
    return combineColorChannels(split_image)
