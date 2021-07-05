import sys
from .imageHandler import asciify
from PIL import Image

def main():
    argv = sys.argv
    try:
        image = Image.open(argv[1])
    except:
        print("Error: Image not found.")
        print("Please refer to the readme file for more information.")
        sys.exit()
    
    try:
        charWidth = int(argv[2])
    except:
        print("Error: Invalid width.")
        print("Please refer to the readme file for more information.")
        sys.exit()
    
    try:
        invert = bool(argv[3])
    except:
        print("Error: The \'Inverted\' arguement is not specified correctly.")
        print("Please refer to the readme file for more information.")
        sys.exit()
    
    print(asciify(charWidth, image, invert))

