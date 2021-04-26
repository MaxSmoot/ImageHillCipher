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
    opts, args = getopt.getopt(argv, "edc", ["key=", "image="])
    for opt, arg in opts:
        if(opt == '-e'):
            encoding = True
        elif(opt == "-d"):
            decoding = True
        elif(opt == "-c"):
            complexKey = True
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
        key = Hill.generateKey(len(image_pixels), len(image_pixels[0]), complexKey)
        encodedImage = Hill.encodeImage(key, padded_image)
        encodedImage.save("Complex-encoded.tiff" if complexKey else "encoded.tiff", None)
        key.save("Complex-key.tiff" if complexKey else "key.tiff", None)

    elif(decoding):
        key_image = Image.open(key_image)
        decodedImage = Hill.decodeImage(key_image, input_image, complexKey)
        decodedImageSave = Image.fromarray(np.uint8(decodedImage))
        decodedImageSave.save("decoded.jpg")


if __name__ == "__main__":
    main(sys.argv[1:])
