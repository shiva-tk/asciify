import sys
from .imageHandler import asciify
from PIL import Image
import argparse

def main():
    parser = argparse.ArgumentParser() 
    parser.add_argument("-i", "--image", type=str, help="The filepath to the image you want to asciify")
    parser.add_argument("-w", "--width", type=int, help="The number of characters wide the output text will be. Defaults to 50.", default=50)
    parser.add_argument("-I", "--inverted", type=bool, help="A boolean representing whether or not the output image should invert black and white. Choose False for black text on white background. Defaults to false.", default=False)

    args = parser.parse_args()
    
    try:
        image = Image.open(args.image)
    except:
        print("usage: asciify [-h] [-i IMAGE] [-w WIDTH] [-I INVERTED]")
        print("asciify: error: image not found")
        sys.exit()
    
    
    print(asciify(args.width, image, args.inverted))

