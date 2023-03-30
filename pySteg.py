import cv2
#useful function def I stole from stack overflow
def string2bits(s=''):
    return [bin(ord(x))[2:].zfill(8) for x in s]
#function to change least significant RGB value
def changeLeastSig(tuple):
    mindex = list(tuple).index(max(tuple))
    if(tuple[mindex] == 0): tuple[mindex] = 1 #we can't have -1 as a color value
    else: tuple[mindex] = tuple[mindex] - 1 
    return tuple
print("Enter the original file name: ")
filename = input()
image = cv2.imread(filename)
rows = len(image)
cols = len(image[0])
print("Image size: ", rows, cols)
print("Theoretical max characters: ", int((rows*cols-18)/8))
print("Program limited max characters: ", pow(2,18)-1)
# We are going to allocate the first 18 bits to tell the program how many ASCII characters are stored
# 262143 is the maximum number of characters that can thus be stored in theory with this model
print("Enter the text you would like to hide: ")
text = input()
btext = string2bits(text)
binaryLength = bin(len(text))[2:] #includes 0b at the start so we have to omit this when editing the image
print(binaryLength)
print(btext)
#for the first 18 pixels
crow, ccol, index = 0, 0, 0
for x in range(0,18):
    if (ccol >= cols):
        crow += 1
        ccol = 0
    if (18-x > len(binaryLength)):
        ccol += 1
        continue
    if (binaryLength[index] == "1"):
            image[crow][ccol] = changeLeastSig(image[crow][ccol])
    index+=1
    ccol += 1
#for the rest
for x in range(0,len(btext)*8):
    if (ccol >= cols):
        crow += 1
        ccol = 0
    if (btext[int(x/8)][x%8] == "1"):
        image[crow][ccol] = changeLeastSig(image[crow][ccol])
    ccol += 1
print("Name of output file: ")
input = input()
cv2.imwrite(input, image)