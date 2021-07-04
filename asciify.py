import sys
import imageHandler
from PIL import Image

argv = sys.argv
try:
    image = Image.open(argv[1])
except:
    print("Error: Image not found.")
    print("Please refer to the readme file for more information.")

try:
    charWidth = int(argv[2])
except:
    print("Error: Invalid width.")
    print("Please refer to the readme file for more information.")

try:
    invert = bool(argv[3])
except:
    print("Error: The \'Inverted\' arguement is not specified correctly.")
    print("Please refer to the readme file for more information.")

print(imageHandler.asciify(charWidth, image, invert))

