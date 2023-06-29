from PIL import Image, ImageDraw, ImageFont
 
# creating a image object (new image object) with
# RGB mode and size 200x200
img = Image.open("file.png")
w=img.size[0]
h=img.size[1]
pixels = img.load()
scale=2
upscaledImg=Image.new(mode="RGB", size=(w*scale, h*scale))
uPixels=upscaledImg.load()
for i in range(h):
    for j in range(w):
        m,n=i*scale, j*scale
        uPixels[m, n]=pixels[i,j]
        uPixels[m+1, n]=pixels[i,j]
        uPixels[m, n+1]=pixels[i,j]
        uPixels[m+1,n+1]=pixels[i,j]
for i in range(h*scale):
    for j in range(w*scale):
        if uPixels[i,j]==(0,0,0):
            uPixels[i,j]=(255,255,255)
# This method will show image in any image viewer
upscaledImg.save("upscaled.png")

