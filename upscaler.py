from PIL import Image, ImageDraw, ImageFont


def scaleImage():
    for i in range(h):
        for j in range(w):
            m, n = i * scale, j * scale
            for dx in range(scale):
                for dy in range(scale):
                    uPixels[m + dx, n + dy] = pixels[j, i]

def fillBlack():
    for i in range(h*scale):
        for j in range(w*scale):
            if uPixels[i,j]==(0,0,0):
                uPixels[i,j]=(255,255,255)


if __name__=="__main__":
    img = Image.open("sample.png")
    w, h=img.size
    pixels = img.load()
    scale=16
    upscaledImg=Image.new(mode="RGB", size=(w*scale, h*scale))
    uPixels=upscaledImg.load()
    scaleImage()
    fillBlack()
    upscaledImg.save("upscaled{}x.png".format(scale))

