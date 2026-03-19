from PIL import Image


def create_blank_canvas():
    """Create blank canvases with different colors."""

    # Create a blank white canvas
    # Image.new(mode, (width, height), color)
    white_canvas = Image.new("RGB", (800, 600), (255, 255, 255))
    white_canvas.save("white_canvas.jpg")
    print("Created white canvas")

    # Create a black canvas
    black_canvas = Image.new("RGB", (800, 600), (0, 0, 0))
    black_canvas.save("black_canvas.jpg")
    print("Created black canvas")

    # Create a colored canvas (light blue for sky)
    blue_canvas = Image.new("RGB", (800, 600), (200, 220, 255))
    blue_canvas.save("blue_canvas.jpg")
    print("Created light blue canvas")

    # Show one of them
    blue_canvas.show()


def paste_image(canvas, source, x_offset, y_offset):
    canvas_pixels = canvas.load()
    source_pixels = source.load()
    src_width, src_height = source.size
    canvas_width, canvas_height = canvas.size

    for x in range(src_width):
        for y in range(src_height):
            # Calculate where this pixel goes on canvas
            dest_x = x_offset + x  # Shift by offset
            dest_y = y_offset + y

            # Check bounds (don't go off canvas!)
            if 0 <= dest_x < canvas_width and 0 <= dest_y < canvas_height:
                # Copy the pixel color
                canvas_pixels[dest_x, dest_y] = source_pixels[x, y]
    return canvas


def create_grid_collage(images, rows, cols, cell_width, cell_height):
    # Calculate total canvas size
    canvas_width = cols * cell_width
    canvas_height = rows * cell_height
    canvas = Image.new("RGB", (canvas_width, canvas_height))
    for i, img in enumerate(images):
        if i >= rows * cols:  # Don't exceed grid capacity
            break
        # Calculate grid position using math trick
        row = i // cols  # Which row? (integer division)
        col = i % cols  # Which column? (remainder)
        x = col * cell_width  # Pixel x position
        y = row * cell_height  # Pixel y position
        # Scale and paste
        scaled = img.resize((cell_width, cell_height))
        canvas = paste_image(canvas, scaled, x, y)
        # canvas.paste(scaled, (x, y))
    return canvas


def create_grid_with_spacing(images, rows, cols, cell_size, spacing):
    canvas_width = cols * cell_size + (cols + 1) * spacing
    canvas_height = rows * cell_size + (rows + 1) * spacing
    canvas = Image.new(
        "RGB", (canvas_width, canvas_height), (240, 240, 240)
    )  # Light gray

    for i, img in enumerate(images):
        if i >= rows * cols:
            break

        row = i // cols
        col = i % cols
        x = (col + 1) * spacing + col * cell_size
        y = (row + 1) * spacing + row * cell_size
        scaled = img.resize((cell_size, cell_size))
        canvas.paste(scaled, (x, y))

    return canvas


def blend_images(img1, img2, alpha):
    width, height = img1.size  # Ensure same size
    img2 = img2.resize((width, height))

    result = Image.new("RGB", (width, height))
    pix1 = img1.load()
    pix2 = img2.load()
    result_pix = result.load()

    for x in range(width):
        for y in range(height):
            r1, g1, b1 = pix1[x, y]
            r2, g2, b2 = pix2[x, y]
            r = int(alpha * r1 + (1 - alpha) * r2)
            g = int(alpha * g1 + (1 - alpha) * g2)
            b = int(alpha * b1 + (1 - alpha) * b2)
            result_pix[x, y] = (r, g, b)

    return result


def chromakey(foreground, background, key_color, threshold=50):
    width, height = foreground.size
    background = background.resize((width, height))
    fg_pixels = foreground.load()
    bg_pixels = background.load()
    
    result = Image.new("RGB", foreground.size)
    result_pixels = result.load()

    for x in range(foreground.size[0]):
        for y in range(foreground.size[1]):
            r, g, b = fg_pixels[x, y]

            # Calculate "color distance" to key color
            # (How different is this pixel from green?)
            distance = (
                abs(r - key_color[0]) + abs(g - key_color[1]) + abs(b - key_color[2])
            )

            if distance < threshold:  # Close to green?
                result_pixels[x, y] = bg_pixels[x, y]  # Use background
            else:  # Not green?
                result_pixels[x, y] = (r, g, b)  # Use foreground

    return result


# img1 = Image.open("beach.jpg").resize((300,300))
# img2 = Image.open("beach.jpg").resize((300,300))
# img3 = Image.open("beach.jpg").resize((300,300))
# img4 = Image.open("beach.jpg").resize((300,300))

img1 = Image.open("beach.jpg")
img2 = Image.open("green.jpg")

canvas = chromakey(img2, img1, (0,255,0), 500)

canvas.show()

# photo = Image.open("beach.jpg")

# # Paste at position (100, 50)
# canvas.paste(photo, (100, 50))

# canvas.save("composition.jpg")
# canvas.show()


# img1 = Image.open("photo1.jpg")
# img2 = Image.open("photo2.jpg")

# # Ensure same size
# img2 = img2.resize(img1.size)

# # Blend with 50/50 mix
# blended = Image.blend(img1, img2, 0.5)

# # More of img2 (alpha = 0.7 means 70% img2, 30% img1)
# blended2 = Image.blend(img1, img2, 0.7)

# blended.save("blended.jpg")
# blended.show()
