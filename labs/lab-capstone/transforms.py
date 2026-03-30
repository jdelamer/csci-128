from PIL import Image


def mirror_horizontal(img):
    """Return a left-right mirrored copy of img."""
    result = img.copy()
    src = img.load()
    dst = result.load()
    w, h = img.size
    for x in range(w):
        for y in range(h):
            # --- YOUR CODE HERE ---
            pass
    return result


def crop(img, x1, y1, x2, y2):
    """Return the rectangular region [x1:x2, y1:y2] of img.

    Parameters
    ----------
    x1, y1 : int   top-left corner of the crop region
    x2, y2 : int   bottom-right corner (exclusive)
    """
    new_w = x2 - x1
    new_h = y2 - y1
    result = Image.new("RGB", (new_w, new_h))
    src = img.load()
    dst = result.load()
    for x in range(new_w):
        for y in range(new_h):
            # --- YOUR CODE HERE ---
            pass
    return result


def scale_down(img, factor):
    """Return a copy of img scaled down by an integer factor.

    Parameters
    ----------
    factor : int   e.g. 2 means half the size in each dimension
    """
    w, h = img.size
    new_w = w // factor
    new_h = h // factor
    result = Image.new("RGB", (new_w, new_h))
    src = img.load()
    dst = result.load()
    for x in range(new_w):
        for y in range(new_h):
            # --- YOUR CODE HERE ---
            pass
    return result


# -------------------------------------------------------
# Apply transformations
# -------------------------------------------------------
original = Image.open("data/photo.jpg")

mirror_horizontal(original).save("output/photo_mirror.jpg")

# Crop the centre quarter of the image
w, h = original.size
crop(original, w // 4, h // 4, 3 * w // 4, 3 * h // 4).save("output/photo_crop.jpg")

scale_down(original, 2).save("output/photo_half.jpg")

print("Transformations saved to output/")
