# Image Hill Cipher

ImageHillCipher is a command-line program that can both encipher and decipher images using a [Hill Cipher](https://www.geeksforgeeks.org/hill-cipher/). ImageHillCipher is written in [Python](https://python.org). This program was developed to demonstrate the versatility of the Hill Cipher with a modern application.

* TOC
\n
{:toc}


## Dependencies

### To Run This Program You Need:

+ [Python 3](https://www.python.org/downloads/)
+ [pip](https://pip.pypa.io/en/stable/installation/)
+ [Pillow](https://python-pillow.org/)
+ [SymPy](https://www.sympy.org/en/index.html)
+ [NumPy](https://numpy.org/)
+ An image viewer that supports .tiff files.

## Installation

1. If not already installed, install [Python 3](https://www.python.org/downloads/).
2. Clone the repository `$ git clone https://github.com/MaxSmoot/ImageHillCipher`
3. [**Optional But Recommended**] Create a [Virtual Environment](https://docs.python.org/3/library/venv.html).
4. Install dependencies
      - ```$ pip install pillow```
      - ```$ pip install symPy```
      - ```$ pip install numPy```

## How To Use

### Required Flags

+ `-e` for encipher mode `-d` for decipher mode. Must specify one or the other.
+ `--image=<path_to_image>` This is the path to the image to encipher or decipher.
+ `--key=<path_to_key>` when using `-d`, this is the path to the key to decipher the image with.

### Optional Flags
+ `--block_size=<positive number>` The size of the key (since the key is square, block_size specifies the length of one of the sides) used for enciphering and deciphering the image. The image will be divided into blocks of size `block_size` and each block will be enciphered or deciphered using the key. When deciphering an image, `block_size` must match the `block_size` specified when enciphering the image. Default `block_size` for enciphering and deciphering is 3.
+ `-c` Program will use a unique key for each `block_size` x `block_size` section of the key instead of tiling the same key. This will massively increase tne time to both encipher and decipher the image. Outputs `complex-enciphered.tiff` and `complex-key.tiff`.

### Enciphering an Image

[In the repo directory] ```$ python3 main.py -e --image=<path_to_image> [--block_size=<int>] [-c]```

If optional arguments are not specified the program uses the quickest method for generating a random key (uniformly applying a single 3x3 key and generating a key image that is that same 3x3 key tiled to match the image dimensions). Outputs `enciphered.tiff and key.tiff`.

### Deciphering an Image

[In the repo directory] ```$ python3 main.py -d --image=<path_to_enciphered_image> --key=<path_to_key> [--block_size=<int>] [-c]```

The program will output `deciphered.jpg`.

## Example

### Enciphering

`test_files/test-medium.jpg`

![test-medium.jpg](https://github.com/MaxSmoot/ImageHillCipher/blob/main/docs/test-medium.jpg?raw=true)

`$ python3 main.py -e --image=test_files/test-medium.jpg`

Output `enciphered.tiff` and `key.tiff`

![enciphered.tiff](https://github.com/MaxSmoot/ImageHillCipher/blob/main/docs/enciphered.png?raw=true)
![key.tiff](https://github.com/MaxSmoot/ImageHillCipher/blob/main/docs/key.png?raw=true)

### Deciphering

`$ python3 main.py -d --image=enciphered.tiff --key=key.tiff`

Output `deciphered.jpg`

![deciphered.tiff](https://github.com/MaxSmoot/ImageHillCipher/blob/main/docs/test-medium.jpg?raw=true)

## FAQS

**Why are the output files when Enciphering .tiff?**

+ In order to decipher the image with the key, all the data needs to be intact. JPEGs and PNGs utilize lossy compression so the data is modified and the image is not able to be deciphered. TIFF utilizes a lossless compression so all the data is intact and deciphering is possible.

**Module Not Found Error**
+ Ensure all dependencies listed in the dependency section are installed. For more information about installing python modules [click here](https://packaging.python.org/tutorials/installing-packages/)

**Enciphering and Deciphering is taking a very long time**
+ Since this program uses complex linear-algebra operations to encipher and decipher, it is best to use images less than 10 megapixels.
+ If `--block_size` was specified to be larger than 3, the program will take significantly longer. Reccomended to use the defaut `block_size`.
+ If the `-c` flag was specified, the program will take **significantly** longer. Try using a smaller image.
