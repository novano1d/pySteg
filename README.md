# pySteg
Basic Steganography with Python. The hidden message must exist between lossless formats (ie PNG not JPG).

## pySteg.py
This Python code provides a simple way to hide text messages within images using the least significant bit (LSB) technique. With this code, you can encode a text message into an image by specifying the image file and the text you want to hide. The code then modifies the pixels in the image to embed the text message using the LSB of each pixel value. The resulting image can be saved as a new file. To decode a hidden message from an encoded image, you can use the same code with the "d" command line argument, and it will extract the hidden text message from the LSBs of the pixel values in the image.

## Example usage:
To encode run `pysteg e` and to decode run `pyteg d`
Both of these will promt the user.