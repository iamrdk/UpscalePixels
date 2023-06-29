from PIL import Image, ImageDraw, ImageFont
import sys
# creating a image object (new image object) with
# RGB mode and size 200x200
w=4
h=4
img = Image.new(mode="RGB", size=(w,h))
pixels = img.load()
for i in range(w):
    for j in range(h):
        if i==0 or i==w-1 or j==0 or j==h-1:
            pixels[i,j]=(0,255,0)
        elif i==j:
            pixels[i,j]=(255,0,0)
        elif (i+j==w-1):
            pixels[i,j]=(0,0,255)
        

# This method will show image in any image viewer
img.save("images/sample.png")