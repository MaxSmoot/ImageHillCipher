# Image Hill Cipher

+ TOC


{:toc}

ImageHillCipher is a command-line program that can both encipher and decipher images using a [Hill Cipher](https://www.geeksforgeeks.org/hill-cipher/). ImageHillCipher is written in [Python](https://python.org). This program was developed to demonstrate the versatility of the Hill Cipher with a modern application.

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
2. Clone the repository `git clone https://github.com/MaxSmoot/ImageHillCipher`
3. [**Optional But Recommended**] Create a [Virtual Environment](https://docs.python.org/3/library/venv.html).
4. Install dependencies
      - `pip install pillow`
      - `pip install symPy`
      - `pip install numPy`

## How To Use

### Required Flags

+ `-e` for encipher mode `-d` for decipher mode. Must specify one or the other.
+ `--image=<path_to_image>` This is the path to the image to encipher or decipher.
+ `--key=<path_to_key>` when using `-d`, this is the path to the key to decipher the image with.
### Optional Flags
+ `--block_size=<positive number>` The size of the key (since the key is square, block_size specifies the length of one of the sides) used for enciphering and deciphering the image. The image will be divided into blocks of size `block_size` and each block will be enciphered or deciphered using the key. When deciphering an image, `block_size` must match the `block_size` specified when enciphering the image. Default `block_size` for enciphering and deciphering is 3.
+ `-c` Program will use a unique key for each `block_size` x `block_size` section of the key instead of tiling the same key. This will massively increase tne time to both encipher and decipher the image. Outputs `complex-enciphered.tiff` and `complex-key.tiff`.

### Enciphering an Image

[In the repo directory] `python3 main.py -e --image=<path_to_image> [--block_size=<int>] [-c]`

If optional arguments are not specified the program uses the quickest method for generating a random key (uniformly applying a single 3x3 key and generating a key image that is that same 3x3 key tiled to match the image dimensions). Outputs `enciphered.tiff and key.tiff`.

### Deciphering an Image

[In the repo directory] `python3 main.py -d --image=<path_to_enciphered_image> --key=<path_to_key> [--block_size=<int>] [-c]`

The program will output `deciphered.jpg`.
