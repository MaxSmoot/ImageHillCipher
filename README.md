# ImageHillCipher
## Encodes and Decodes .jpg images using a Hill Cipher

## How To Use
**Images Must be in the .jpg or .tiff format**

**Images whose dimensions are >300 x >300 will encode/decode slowly**
### Encoding
`python3 main.py -e --image=<image>`
This will output, in the same directory: **encoded.tiff** and **key.tiff**

### Decoding
`python3 main.py -d --image=<encoded image> --key=<key>`
This will output, in the same directory: **decoded.jpg**

## Dependencies
- python 3
- numPy
- sympy
- Pillow
