from PIL import Image
import numpy as np
from sympy import Matrix


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


def combineColorChannels(imagearr):
    combined = np.empty((len(imagearr["red"]), len(
        imagearr["red"]), 3))
    for i in range(0, len(imagearr["red"])):
        for j in range(0, len(imagearr["red"][0])):
            combined[i, j] = imagearr["red"][i,
                                             j], imagearr["green"][i, j], imagearr["blue"][i, j]
    return combined


def matrixMultImage(key, image):

    split_image = extractColorChannels(image)

    i = 0
    j = 0
    size = len(split_image["red"])
    while(i < size):
        while(j < size):
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


def matrixInverseImage(image):
    split_colors = extractColorChannels(image)
    inverse_colors = {"red": np.array(Matrix(split_colors["red"]).inv_mod(255)), "green": np.array(Matrix(
        split_colors["green"]).inv_mod(255)), "blue": np.array(Matrix(split_colors["blue"]).inv_mod(255))}
    return combineColorChannels(inverse_colors)
