from PIL import Image

img = Image.new("RGB", (500, 400), (200, 200, 200))
r, g, b = img.getpixel((10,10))
print(r,g,b)
for x in range(250):
    for y in range(400):
        img.putpixel((x,y), (128, 128, 0))

for x in range(250, 500):
    for y in range(400):
        img.putpixel((x,y), (0, 0, 255))




img.show()