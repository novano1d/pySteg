import cv2
import numpy as np
#another function I stole from stack overflow
def bits2string(b=None):
    return ''.join([chr(int(x, 2)) for x in b])
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