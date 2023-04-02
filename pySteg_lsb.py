import cv2
import numpy as np
#useful function def I stole from stack overflow
def string2bits(s=''):
    return [bin(ord(x))[2:].zfill(8) for x in s]
#change remainder
def makeRemainder(remainder, num):
    if(num == 255): num = 254
    while(num%2 != remainder):
        num+=1
    return num
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