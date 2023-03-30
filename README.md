# pySteg
Basic Steganography with Python
## pySteg.py
This Python code is a simple implementation of a steganography software that hides a user-provided message inside an image by altering the least significant bit of its RGB values. The program asks the user for the name of the original file and the message to hide, which it then converts into binary using the string2bits function. The first 18 pixels of the image are used to store the length of the message in binary format, which is limited to 262143 characters. If necessary, you could modify the code so that more pixels are used to store the length of the message and this would allow the algorithm to accomidate more characters. The program then loops through the remaining pixels of the image and replaces the least significant bit of the RGB values with the message bits. Finally, the modified image is saved with a user-provided name. This is a simple but effective way of hiding messages in images, although it may be vulnerable to attacks that analyze the statistical properties of the modified image.

## pyStegDecrypt.py
This Python code is a complementary part of a steganography software that retrieves a hidden message from an image. The program asks the user to provide two images, one of which contains the hidden message. It then calculates the absolute difference between the RGB values of the two images and searches the first 18 pixels of the difference image to extract the binary representation of the number of characters in the hidden message. The program then loops through the remaining pixels of the difference image, extracts the hidden message bits, and saves them in an array of binary strings. Finally, the binary message is converted to a string using the bits2string function and printed to the console. This program can successfully extract hidden messages from images generated using the previous Python script in this repository.
