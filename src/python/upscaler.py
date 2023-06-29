from PIL import Image
import numpy as np
from time import time
def scaleImage():
    for i in range(h):
        for j in range(w):
            u_pixels[i * scale:(i + 1) * scale, j * scale:(j + 1) * scale] = pixels[i, j]

def fillBlack():
    black_pixels = np.all(u_pixels == (0, 0, 0), axis=2)
    u_pixels[black_pixels] = (255, 255, 255)

if __name__ == "__main__":
    start=time()
    img = Image.open("images/pexels.jpg")
    w, h = img.size
    pixels = np.array(img)
    print("Time taken to load image of size {}x{}: {} seconds".format(h,w,time()-start))
    start=time()
    scale = 3
    upscaled_img = Image.new(mode="RGB", size=(w * scale, h * scale))
    u_pixels = np.array(upscaled_img)
    print("Time taken to create new image of size {}x{}: {} seconds".format(h*scale,h*scale,time()-start))
    start=time()
    scaleImage()
    print("Time taken to scale image {} times: {} seconds".format(scale,time()-start))
    start=time()
    fillBlack()
    print("Time taken to fill black: {} seconds".format(time()-start))

    upscaled_img = Image.fromarray(u_pixels)
    upscaled_img.save("output/upscaled{}x.jpg".format(scale))
