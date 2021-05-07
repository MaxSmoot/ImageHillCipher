# ImageHillCipher
## Encrypts and Decrypts .jpg images using a Hill Cipher

## How To Use
**Images Must be in the .jpg or .tiff format**

**Example** 

**Encrypting**
`python3 main.py -e --image=test_files/test-large.jpg`

**Decrypting**
`python3 main.py -d --image=encyrpted.tiff --key=key.tiff`

### Encrypting
`python3 main.py -e [-c] [--block_size=<int>] --image=<image>`
This uses the quickest method for generating a random key (uniformly applying a single 3x3 key)

This will output, in the same directory: **encrypted.tiff** and **key.tiff**

### Decrypting

`python3 main.py -d [-c] [--block_size=<int>] --image=<encrypted image> --key=<key>`
This will output, in the same directory: **decrypted.jpg**


### Optional Flags (Must match when Encrypting and Decrypting)

- `--block_size=<int>` The size of the key and the subsize of the image that will be encrypted in blocks (Must be positive, generally anything larger than 15 will take a lot of time). The image will be padded with black to ensure width and length are evenly divisible by the block_size.

- `-c` Will use a unique key for every subsection of the image instead of uniformly applying a single key. **This will massively increase time to compute**. Outputs **Complex-encrypted-tiff** and **Complex-key.tiff**

## Dependencies
- python 3
- numPy
- sympy
- Pillow
