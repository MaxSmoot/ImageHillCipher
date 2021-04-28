from PIL import Image
import numpy as np
from sympy import Matrix
import HillCipher as Hill
import ImageManip as IManip
import sys
import getopt


def main(argv):
    encoding = False
    decoding = False
    complexKey = False
    input_image = None
    key_image = None
    block_size = 3
    opts, args = getopt.getopt(argv, "edcb", ["key=", "image=", "block_size="])
    for opt, arg in opts:
        if(opt == '-e'):
            encoding = True
        elif(opt == "-d"):
            decoding = True
        elif(opt == "-c"):
            complexKey = True
            print("Using nonuniform encryption, this will take much longer")
        elif(opt == "--block_size"):
            block_size = int(arg)
            if(block_size < 0):
                print("block_size must be a positive integer")
            elif(block_size > 10):
                print("large block_sizes will increase compute time")
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
        print("Encrypting... Will output to:", "Complex-encoded.tiff" if complexKey else "encoded.tiff",
              "Complex-key.tiff" if complexKey else "key.tiff")
        padded_image = IManip.padImage(image_pixels, block_size)
        image_pixels = np.array(padded_image)
        key = Hill.generateKey(len(image_pixels), len(
            image_pixels[0]), block_size, complexKey)
        encodedImage = Hill.encodeImage(key, padded_image, block_size)
        encodedImage.save(
            "Complex-encoded.tiff" if complexKey else "encoded.tiff", None)
        key.save("Complex-key.tiff" if complexKey else "key.tiff", None)
        print("Success!")

    elif(decoding):
        print("Decoding... Will output to: Decoded.jpg")
        print("All optional flags must match the original encryption")
        key_image = Image.open(key_image)
        decodedImage = Hill.decodeImage(
            key_image, input_image, block_size, complexKey)
        decodedImageSave = Image.fromarray(np.uint8(decodedImage))
        decodedImageSave.save("decoded.jpg")
        print("Success!")


if __name__ == "__main__":
    main(sys.argv[1:])
