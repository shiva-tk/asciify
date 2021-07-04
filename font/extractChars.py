from PIL import Image
import os

im = Image.open("TamzenForPowerline7x14r.png")

chars = [im.crop((7*(i % 32), 14*(i//32), 7*(i%32)+7, 14*(i//32)+ 14)) for i in range(0, 224)]

dirname = os.path.dirname(__file__)
for i in range(len(chars)):
    outfile = os.path.join(dirname, "chars/"+str(i) + ".png")
    chars[i].save(outfile)
