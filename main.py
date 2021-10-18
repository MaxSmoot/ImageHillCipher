from PIL import Image
import numpy as np
import HillCipher as Hill
import ImageManip as IManip
import sys
import getopt


def main(argv):
    #The mode for the program
    enciphering = False
    deciphering = False

    #complexKey, when true, uses a unique block_size x block_size key for each block_size x block_size section of the image
    #false by default since its computationally expsensive
    complexKey = False
    input_image = None
    key_image = None
    #default block size is 3
    #size of the key that is tiled to form the key Image
    block_size = 3
    try: 
        opts, _ = getopt.getopt(argv, "edcb", ["key=", "image=", "block_size="])
    except Exception as e:
        print("Error:", e)
        sys.exit()
    
    for opt, arg in opts:
        if(opt == '-e'):
            enciphering = True
        elif(opt == "-d"):
            deciphering = True
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
    if(enciphering == deciphering):
        print("Error: must specify either -e or -d")
        sys.exit()
    try:
        input_image = Image.open(input_image)
        image_pixels = np.array(input_image)
    except Exception as e:
        print("Error opening image", e)
        sys.exit()

    if(enciphering):
        enciphered_filename = "complex-enciphered.tiff" if complexKey else "enciphered.tiff"
        key_filename = "complex-key.tiff" if complexKey else "key.tiff"
        print("Enciphering... Will output to:", enciphered_filename, "and", key_filename)
        padded_image = IManip.padImage(image_pixels, block_size)
        image_pixels = np.array(padded_image)
        key = Hill.generateKey(len(image_pixels), len(
            image_pixels[0]), block_size, complexKey)
        enciphered_image = Hill.encipherImage(key, padded_image, block_size)
        enciphered_image.save(
            enciphered_filename, None)
        key.save(key_filename, None)
        print("Success!")

    elif(deciphering):
        print("Decrypting... Will output to: deciphered.jpg")
        print("All optional flags must match flags used when enciphering")
        try: 
            key_image = Image.open(key_image)
        except Exception as e:
            print("Error reading key:", e)
            sys.exit()
        deciphered_image = Hill.decipherImage(
            key_image, input_image, block_size, complexKey)
        deciphered_image.save("deciphered.jpg")
        print("Success!")


if __name__ == "__main__":
    main(sys.argv[1:])
