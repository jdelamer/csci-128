from PIL import Image


def grayscale(img):
    """Return a grayscale copy of img.

    Use the standard luminance formula to convert each pixel to gray.
    """
    result = img.copy()
    pixels = result.load()
    w, h = result.size
    for x in range(w):
        for y in range(h):
            r, g, b = pixels[x, y]
            # --- YOUR CODE HERE ---
            pass
    return result


def negative(img):
    """Return a negative copy of img."""
    result = img.copy()
    pixels = result.load()
    w, h = result.size
    for x in range(w):
        for y in range(h):
            r, g, b = pixels[x, y]
            # --- YOUR CODE HERE ---
            pass
    return result


def adjust_brightness(img, amount):
    """Return a copy of img with brightness shifted by amount.

    Parameters
    ----------
    img    : PIL Image
    amount : int   positive = brighter, negative = darker
    """
    result = img.copy()
    pixels = result.load()
    w, h = result.size
    for x in range(w):
        for y in range(h):
            r, g, b = pixels[x, y]
            # --- YOUR CODE HERE ---
            pass
    return result


def tint(img, tr, tg, tb):
    """Return a copy of img with a colour tint applied.

    Each channel should be scaled by its corresponding factor
    (tr, tg, tb), then clamped to [0, 255].
    """
    result = img.copy()
    pixels = result.load()
    w, h = result.size
    for x in range(w):
        for y in range(h):
            r, g, b = pixels[x, y]
            # --- YOUR CODE HERE ---
            pass
    return result


# -------------------------------------------------------
# Apply and save all four filters
# -------------------------------------------------------
original = Image.open("data/photo.jpg")

grayscale(original).save("output/photo_gray.jpg")
negative(original).save("output/photo_negative.jpg")
adjust_brightness(original, 50).save("output/photo_bright.jpg")
adjust_brightness(original, -50).save("output/photo_dark.jpg")
tint(original, 1.0, 0.7, 0.7).save("output/photo_warm.jpg")

print("All filters saved to output/")
