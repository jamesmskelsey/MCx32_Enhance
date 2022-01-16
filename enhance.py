from PIL import Image
from PIL.ImageOps import scale
import os

files = os.listdir()
files = list(file for file in files if file[-4:] == ".png")

print("Found these files to modify: ", files)

x16 = (16, 16)

for file in files:
    im = Image.open(file)
    is16x = im.size == x16
    if is16x:
        # double the image in size to 32 by 32
        out = scale(im, 2)
        # save it as the original name
        out.save(f"{file[:-4]}_x32.png", "PNG")
