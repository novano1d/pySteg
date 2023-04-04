import cv2
import numpy as np
import sys
#useful function def I stole from stack overflow
def string2bits(s=''):
    return [bin(ord(x))[2:].zfill(8) for x in s]
def bits2string(b=None):
    return ''.join([chr(int(x, 2)) for x in b])
#change remainder
def makeRemainder(remainder, num):
    if(num == 255): num = 254
    while(num%2 != remainder):
        num+=1
    return num

if (len(sys.argv) == 2):
    if (sys.argv[1] == "e"):
        print("Enter the original file name: ")
        filename = input()
        image = cv2.imread(filename)
        unwound = np.ravel(image)
        print("Max insertable characters:", int(len(unwound)/8-1))
        print("Enter the text you would like to hide: ")
        text = input()
        btext = string2bits(text)
        print(btext)
        for x in range(0,len(btext)*8):
            if (unwound[x] % 2 == 0 and btext[int(x/8)][x%8] == '1'):
                unwound[x] = makeRemainder(1, unwound[x])
            if (unwound[x] % 2 == 1 and btext[int(x/8)][x%8] == '0'):
                unwound[x] = makeRemainder(0, unwound[x])
        for x in range(len(btext)*8,len(btext)*8+8):
            if (unwound[x] % 2 == 1):
                unwound[x] = makeRemainder(0, unwound[x])
        rewoundImg = np.reshape(unwound, image.shape)
        print("Name of output file: ")
        input = input()
        cv2.imwrite(input, rewoundImg)
    elif (sys.argv[1] == "d"):
        print("Enter the name of the image to decrypt:")
        messagepth = input()
        image = cv2.imread(messagepth)
        binMsg = []
        char = ''
        image = np.ravel(image)
        i = 0
        while (char != "00000000"):
            if (i%8==0): char = ''
            if (image[i]%2 == 1): char += '1'
            else: char += '0'
            if (i%8==7): 
                binMsg.append(char)
            i+=1
        print(binMsg)
        print("Message:", bits2string(binMsg))
else:
    print("Use command line argument \"e\" and \"d\" for encode and decode respectively.")