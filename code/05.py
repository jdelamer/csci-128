from PIL import Image

def greet(name):
    message = "Hello, " + name
    return message

def add(a, b):
    print("test")
    result = a + b
    return result

def double(x):
    result = 2 * x
    return result

def average(a,b):
    result = (a + b) /2
    return result

# print(double(5))
# print(double(21))

# print(average(15,20))

def copy_image(src_image):
    width, height = src_image.size
    new_img = Image.new ("RGB", ( width , height ) )

    src_pixel = src_image.load()
    dst_pixel = new_img.load()

    for x in range(width):
        for y in range(height):
            dst_pixel[x, y] = src_pixel[x, y]
    
    return new_img

def mirror_vertical(src_image):
    width, height = src_image.size
    new_img = Image.new ("RGB", ( width , height ) )

    src_pixel = src_image.load()
    dst_pixel = new_img.load()

    for x in range(width):
        for y in range(height):
            src_x = width - 1 - x  
            dst_pixel[x, y] = src_pixel[src_x, y]
    
    return new_img

def mirror_horizontal(src_image):
    width, height = src_image.size
    new_img = Image.new ("RGB", ( width , height ) )

    src_pixel = src_image.load()
    dst_pixel = new_img.load()

    for x in range(width):
        for y in range(height):
            src_y = height - 1 - y  
            dst_pixel[x, y] = src_pixel[x, src_y]
    
    return new_img


def rotate_90_clockwise(img):
    """Rotate image 90 degrees clockwise"""
    width, height = img.size
    rotated = Image.new("RGB", (height, width)) # Dimensions are swapped!

    src_pixels = img.load()
    dst_pixels = rotated.load()

    for x in range(width):
        for y in range(height):
            color = src_pixels[x, y]
            # Transform coordinates
            new_x = height - 1 - y
            new_y = x
            dst_pixels[new_x, new_y] = color

    return rotated

def rotate_90_counter_clockwise(img):
    """Rotate image 90 degrees counter-clockwise"""
    width, height = img.size
    rotated = Image.new("RGB", (height, width))

    src_pixels = img.load()
    dst_pixels = rotated.load()

    for x in range(width):
        for y in range(height):
            color = src_pixels[x, y]
            # Different transformation
            new_x = y
            new_y = width - 1 - x
            dst_pixels[new_x, new_y] = color

    return rotated

def rotate_180(img):
    """Rotate image 90 degrees counter-clockwise"""
    width, height = img.size
    rotated = Image.new("RGB", (width, height))

    src_pixels = img.load()
    dst_pixels = rotated.load()

    for x in range(width):
        for y in range(height):
            color = src_pixels[x, y]
            # Different transformation
            new_x = width - 1 - x
            new_y = height - 1 - y
            dst_pixels[new_x, new_y] = color

    return rotated

def crop_image(img, start_x, start_y, width, height):
    """Crop a rectangular region from an image"""
    # Create new image with crop dimensions
    cropped = Image.new("RGB", (width, height))
    src_pixels = img.load()
    dst_pixels = cropped.load()

    # Copy the selected region
    for x in range(width):
        for y in range(height):
            # Read from offset position in source
            color = src_pixels[start_x + x, start_y + y]
            # Write to normal position in destination
            dst_pixels[x, y] = color

    return cropped

def scale_by_factor(img, factor):
    """Scale image by a multiplication factor"""
    width, height = img.size
    new_width = int(width * factor)
    new_height = int(height * factor)
    return img.resize((new_width, new_height))

def scale_to_width(img, new_width):
    """Scale image to specific width, maintain aspect ratio"""
    width, height = img.size
    factor = new_width / width
    new_height = int(height * factor)
    return img.resize((new_width, new_height))


img = Image.open("beach.jpg")
img.show()
new_image = scale_by_factor(img, 2)
new_image.show()
