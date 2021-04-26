from PIL import Image
import numpy as np
from sympy import Matrix
import HillCipher as Hill
import ImageManip as IManip
import sys
import getopt
original_image = Image.open('image.jpeg')
image_pixels = np.array(original_image)


def encodeImage(key, image):
    multiplied = IManip.matrixMultImage(key, image)
    return np.mod(multiplied, 256)


def decodeImage(key, image):
    return encodeImage(Hill.invertKey(key), image)


def main(argv):
    encoding = False
    decoding = False
    input_image = None
    key_image = None
    opts, args = getopt.getopt(argv, "ed", ["key=", "image="])
    for opt, arg in opts:
        if(opt == '-e'):
            encoding = True
        elif(opt == "-d"):
            decoding = True
        if(opt == "--image"):
            input_image = arg
            if(not (arg.endswith(".jpg") or arg.endswith(".tiff"))):
                print("image must be jpg or tiff")
                sys.exit()
        if(opt == "--key"):
            key_image = arg

    if(not(encoding != decoding)):
        print("must specify either -e or -d")
        sys.exit()
    input_image = Image.open(input_image)
    image_pixels = np.array(input_image)
    if(encoding):
        padded_image = IManip.padImage(image_pixels)
        image_pixels = np.array(padded_image)
        key = Hill.generateKey(len(image_pixels), len(image_pixels[0]))
        encodedImage = encodeImage(key, image_pixels)
        encodedSave = Image.fromarray(np.uint8(encodedImage))
        encodedSave.save("encoded.tiff", None)
        key = IManip.combineColorChannels(
            {"red": key, "green": key, "blue": key})
        keySave = Image.fromarray(np.uint8(key))
        keySave.save("key.tiff", None)

    elif(decoding):
        key_image = Image.open(key_image)
        key_pixels = np.array(key_image)
        key = Hill.extractKey(key_pixels)
        decodedImage = decodeImage(key, image_pixels)
        decodedImageSave = Image.fromarray(np.uint8(decodedImage))
        decodedImageSave.save("decoded.jpg")


if __name__ == "__main__":
    main(sys.argv[1:])
