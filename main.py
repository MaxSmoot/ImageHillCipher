from PIL import Image
import numpy as np
import HillCipher as Hill
import ImageManip as IManip
import sys
import getopt


def main(argv):
    encrypting = False
    decrypting = False
    complexKey = False
    input_image = None
    key_image = None
    ##default block size is 3
    block_size = 3

    try: 
        opts, _ = getopt.getopt(argv, "edcb", ["key=", "image=", "block_size="])
    except Exception as e:
        print("Error:", e)
        sys.exit()
    
    for opt, arg in opts:
        if(opt == '-e'):
            encrypting = True
        elif(opt == "-d"):
            decrypting = True
        elif(opt == "-c"):
            complexKey = True
            print("Warning: Using nonuniform encryption, this will take much longer")
        elif(opt == "--block_size"):
            block_size = int(arg)
            if(block_size < 0):
                print("Error: block_size must be a positive integer")
            elif(block_size > 10):
                print("Warning: large block_sizes will increase compute time")
        elif(opt == "--image"):
            input_image = arg
            if(not (arg.endswith(".jpg") or arg.endswith(".tiff"))):
                print("Error: image must be jpg or tiff")
                sys.exit()
        elif(opt == "--key"):
            key_image = arg

    # must specify one or the other but not both
    if(encrypting == decrypting):
        print("Error: must specify either -e or -d")
        sys.exit()
    try:
        input_image = Image.open(input_image)
        image_pixels = np.array(input_image)
    except Exception as e:
        print("Error opening image(s)", e)
        sys.exit()
    if(encrypting):
        print("Encrypting... Will output to:", "Complex-encrypted.tiff" if complexKey else "encrypted.tiff",
              "Complex-key.tiff" if complexKey else "key.tiff")
        padded_image = IManip.padImage(image_pixels, block_size)
        image_pixels = np.array(padded_image)
        key = Hill.generateKey(len(image_pixels), len(
            image_pixels[0]), block_size, complexKey)
        encodedImage = Hill.encodeImage(key, padded_image, block_size)
        encodedImage.save(
            "Complex-encrypted.tiff" if complexKey else "encrypted.tiff", None)
        key.save("Complex-key.tiff" if complexKey else "key.tiff", None)
        print("Success!")

    elif(decrypting):
        print("Decrypting... Will output to: Decrypted.jpg")
        print("All optional flags must match the original encryption")
        try: 
            key_image = Image.open(key_image)
        except Exception as e:
            print("Error reading key:", e)
            sys.exit()
        decryptedImage = Hill.decodeImage(
            key_image, input_image, block_size, complexKey)
        decryptedImageSave = Image.fromarray(np.uint8(decryptedImage))
        decryptedImageSave.save("decrypted.jpg")
        print("Success!")


if __name__ == "__main__":
    main(sys.argv[1:])
