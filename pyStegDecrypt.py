import cv2
import numpy as np
#another function I stole from stack overflow
def bits2string(b=None):
    return ''.join([chr(int(x, 2)) for x in b])
print("Enter the name of the first image: ")
messagepth = input()
image1 = cv2.imread(messagepth)
print("Enter the name of the second image: ")
messagepth = input()
image2 = cv2.imread(messagepth)
diff = cv2.absdiff(image1, image2)
rows = len(diff)
cols = len(diff[0])
numOfCharacters = ''
crow, ccol = 0, 0
for x in range(0,18):
    if (ccol >= cols):
        crow += 1
        ccol = 0
    if (np.any(diff[crow][ccol])):
        numOfCharacters += '1'
    else:
        numOfCharacters += '0'
    ccol += 1
print("Number of characters in message:", int(numOfCharacters,2))
print(numOfCharacters)
binMsg = []
char = ''
for x in range(0,int(numOfCharacters,2)*8):
    if (ccol >= cols):
        crow += 1
        ccol = 0
    if (np.any(diff[crow][ccol])):
        char += '1'
    else:
        char += '0'
    ccol += 1
    if(x%8==7):
        binMsg.append(char)
        char = ''
print(binMsg)
print("Message:", bits2string(binMsg))