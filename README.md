# ImageHillCipher
## Encodes and Decodes .jpg images using a Hill Cipher

## How To Use
**Images Must be in the .jpg or .tiff format**

**Images whose dimensions are > 300x300 will encode/decode slowly when using complex encyprtion**

### Encoding
`python3 main.py -e [-c]--image=<image>`
This uses the quickest method for generating a random key (uniform key)

This will output, in the same directory: **encoded.tiff** and **key.tiff**

For a more robust encryption (non-uniform key) use `-c` flag, this will output **Complex-encoded.tiff** and **Complex-key.tiff**  

**Complex key generation takes much longer to compute**

**To decode a Complex encoded image with a Complex encoded key you must use `-c` when decoding**



### Decoding

`python3 main.py -d [-c] --image=<encoded image> --key=<key>`
This will output, in the same directory: **decoded.jpg**

## Dependencies
- python 3
- numPy
- sympy
- Pillow
