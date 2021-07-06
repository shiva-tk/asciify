from PIL import Image
import math
from .getCharBrightness import getCharBrightness

def convertMonoChrome(image):
    #Takes in an image, returns an image which is converted to monochrome
    image = image.convert("L")
    return image

def asciify(charWidth, image, invert):
    image = convertMonoChrome(image)
    pixelWidth, pixelHeight = image.size
    ratio = pixelHeight / pixelWidth
    charHeight = int(ratio * charWidth * 0.5)
    pixelsPerCharacter = int(pixelWidth / charWidth)
    
    charMap = [["" for i in range(charWidth)] for i in range(charHeight)]
    
    characters = getCharBrightness()
    if invert: characters.reverse()
    for y in range(charHeight):
        for x in range(charWidth):
            crop = image.crop((pixelsPerCharacter * x, pixelsPerCharacter * y * 2, pixelsPerCharacter * (x + 1), pixelsPerCharacter * (y + 1) * 2))
            pixels = list(crop.getdata())
            brightness = sum(pixels) / len(pixels)
            brightness *= 1/255
            brightness = sigmoid(brightness)
            brightness *= 255
            brightness = int(brightness / 255 * (len(characters) - 1))
            character = characters[brightness]
            charMap[y][x] = character[0]

    for i in range(len(charMap)):
        charMap[i] = "".join(charMap[i])
    charMap = "\n".join(charMap)

    return charMap
            


def sigmoid(x):
    x = math.e ** (-10*x + 5)
    x += 1
    x = 1/x
    return x
    
