from PIL import Image
import numpy as np

def padImage(image, factor):
    '''
    Convert an image to an image padded with black whose dimensions are evenly divisible by factor. If the image is already evenly divisible by factor it returns the original image

    Args:
        image (PIL.Image): Image to pad
        factor (int): The number the width and height of the image must be evenly divisible by

    Returns:
        PIL.Image: The padded image

    '''
    hlength = len(image)
    vlength = len(image[0])
    if(hlength % factor != 0):
        buffer_col = np.full((1, vlength, 3), 0, dtype="uint8")
        for _ in range(0, factor - (hlength % factor)):
            image = np.vstack((image, buffer_col))
            hlength += 1
    if(vlength % factor != 0):
        buffer_row = np.full((hlength, 1, 3), 0, dtype="uint8")
        for _ in range(0, factor - (vlength % factor)):
            image = np.hstack((image, buffer_row))
            vlength += 1
    return Image.fromarray(image)



def matrixMultImage(key, image, block_size):
    '''
    Left Multiply 3x3 chunks of the image by corresponding 3x3 chunks of the key.
    Multiplies all the color channels by the key then combines into an Image.

    Args:
        key (PIL.Image): The key image to multiply image by
        image (PIL.Image): The image to multiply by the key
        block_size (int): The size of the subkey tiled to form the key image

    Returns:
        PIL.Image: The resulting image from computing key.image
    ''' 
    colorChannels = image.split()
    encryptedChannels = []
    #since the key is greyscale we only use a single color channel
    key = np.array(key.split()[0])
    i = 0
    j = 0
    for colorChannel in colorChannels:
        colorChannel = np.array(colorChannel)
        while(i < len(colorChannel)):
            while(j < len(colorChannel[0])):
                colorChannel[i:i+block_size, j:j+block_size] = np.matmul(key[i:i+block_size, j:j+block_size], colorChannel[i:i+block_size, j:j+block_size])
                j += block_size
            i += block_size
            j = 0
        i = 0
        encryptedChannels.append(Image.fromarray(colorChannel))
    return Image.merge('RGB', encryptedChannels)
