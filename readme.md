# MCx32_Enhance

This is a small project to convert Minecraft 16x textures to 32x textures. The use case: I found a texture pack that I really like in 32x called [Conquest](https://conquestreforged.com/conquest-pack).
There's a mod called [tetra](https://github.com/mickelus/tetra) that lets you reconfigure weapons
and tools.

They don't play together very well. Tetra uses copies of textures to build up the items. So I want to create a texture pack
that replaces those textures with pieces of items from Conquest.

Step one? Take the 16x texture, double it in size to 32x, save it as png. Not terribly hard, but pretty boring to do for hundreds of images. Granted, I could do that for each image as I go... or I can play with python and have it done when I get there.

Step two is much more manual. Cut part of another texture out and plop it down on a layer underneath the old texture, erase unneeded parts (say, for example, the hilt from sword texture on an image that supposed to only be the blade). I don't mind doing that part myself.

### Release 1:

---

~~Upsize a supplied texture from 16x to 32x, resample so that the image is basically the same.~~

### Release 2:

---

~~Upsize all of the images in a folder, and all the subfolders.~~

### Release 3:

---

Take an already modified \_left side of a double sided tool, flip it, rotate it 90 degrees ↩️, and save it as the \_right side of that tool.

### Release 4:

---

Release as a package so I can have it installed globally.
