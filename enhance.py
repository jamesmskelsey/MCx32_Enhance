from PIL import Image
from PIL.ImageOps import scale
import os
import sys
from files import get_files


def resize_and_save(filename):
    x16 = (16, 16)
    im = Image.open(filename)
    is16x = im.size == x16
    if is16x:
        # double the image in size to 32 by 32
        out = scale(im, 2)
        # save it as the original name (I'm appending x32 to test)
        out.save(f"{filename[:-4]}_x32.png", "PNG")

# All folders/files?
walk = "-w" in sys.argv

if walk:
    data = os.walk(os.getcwd())
    print("Found these files to modify: ")
    for root, dirs, files in data:
        # separate out the files, dirs, root
        files = [f for f in files if not f[0] == '.']
        files = [f for f in files if f[-4:] == '.png']
        dirs[:] = [d for d in dirs if not d[0] == '.']

        # now we can use them - we'll need to modify the images while
        # we're in the folder
        print(root, dirs, files)
        for file in files:
            filename = f"{root}\{file}"
            resize_and_save(filename)

else:
    # get the files in the cwd, resize and save each one
    files = get_files()
    for file in files:
        resize_and_save(file)


#

#
#
