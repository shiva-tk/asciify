from PIL import Image
import os

#Creates a lookup table to match character number to character.

def getCharBrightness():
    characterLookup = [" " for i in range(224)]
    characterAverageBrightness = [0 for i in range(224)]
    
    for i in range(32, 32+26):
        characterLookup[i] = chr(65-32 + i)
    
    for i in range(32+27, 64):
        characterLookup[i] = str(i - (32+26))
    
    for i in range(64, 64+26):                                                                            
        characterLookup[i] = chr(97-64 + i) 
    
    for i in range(64+27, 96):
        characterLookup[i] = str(i - (64+26))
    
    
    characterLookup[96] = "{"
    characterLookup[97] = "}"
    characterLookup[98] = "["
    characterLookup[99] = "]"
    characterLookup[100] = "("
    characterLookup[101] = ")"
    characterLookup[102] = "<"
    characterLookup[103] = ">"
    characterLookup[104] = "$"
    characterLookup[105] = "*"
    characterLookup[106] = "-"
    characterLookup[107] = "+"
    characterLookup[108] = "="
    characterLookup[109] = "/"
    characterLookup[110] = "#"
    characterLookup[111] = "_"
    characterLookup[112] = "%"
    characterLookup[113] = "^"
    characterLookup[114] = "@"
    characterLookup[115] = "\\"
    characterLookup[116] = "&"
    characterLookup[117] = "|"
    characterLookup[118] = "~"
    characterLookup[119] = "?"
    characterLookup[120] = "\'"
    characterLookup[121] = "\""
    characterLookup[122] = "`"
    characterLookup[123] = "!"
    characterLookup[124] = ","
    characterLookup[125] = "."
    characterLookup[126] = ";"
    characterLookup[127] = ":"
    
    dirname = os.path.dirname(__file__)
    for i in range (32, 128):
        fileName = os.path.join(dirname, "font/chars/"+ str(i) + ".png")
        im = Image.open(fileName)
        pixels = list(im.getdata(0))
        average = sum(pixels)/ len(pixels)
        characterAverageBrightness[i] = average
    
    
    characters = [(characterLookup[i], characterAverageBrightness[i]) for i in range(224)]
    
    characters.sort(key=lambda a: a[1])
    
    characters = characters[128:223]
    
    return characters
