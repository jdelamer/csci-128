from PIL import Image

# my_image = Image.open("beach.jpg")
# pixels = my_image.load()
# width, height = my_image.size

# for x in range(width):
#     for y in range(height):
#         (r, g, b) = pixels[x, y]

#         new_r = int(r*0.299)
#         new_g = int(g*0.587)
#         new_b = int(0.114*b)

#         gray = int(new_r+new_g+new_b)

#         pixels[x, y] = (gray, gray, gray)

# my_image.show()

my_image = Image.open("beach.jpg")
pixels = my_image.load()
width, height = my_image.size

for x in range(width):
    for y in range(height):
        (r, g, b) = pixels[x, y]

        if r > b:
            pixels[x, y] = (255, 0, 0)
        else:
            pixels[x, y] = (0, 0, 255)

my_image.show()



