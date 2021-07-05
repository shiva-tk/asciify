import sys
from .imageHandler import asciify
from PIL import Image
import argparse

def main():
    parser = argparse.ArgumentParser 
    parser.add_argument("-i", "--image", type=str, help="The filepath to the image you want to asciify")
    parser.add_argument("-w", "--width", type=int, help="The number of characters wide the output text will be. Defaults to 50.", default=50)
    parser.add_argument("-I", "--inverted", type=bool, help="A boolean representing whether or not the output image should invert black and white. Choose False for black text on white background.", default=False)
    
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

