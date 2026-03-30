import csv
import os

from PIL import Image

BADGE_W = 300
BADGE_H = 150
COLS = 5  # number of columns in the grid
PADDING = 10  # pixels of space between badges
BG_COLOUR = (30, 30, 30)  # dark background


def build_collage(badge_paths, cols, badge_w, badge_h, padding, bg):
    """Arrange badge images in a grid and return the canvas.

    Parameters
    ----------
    badge_paths : list of str    paths to individual badge images
    cols        : int            number of columns
    badge_w, badge_h : int       expected size of each badge
    padding     : int            gap between badges (pixels)
    bg          : tuple          background RGB colour

    Returns
    -------
    PIL Image
    """
    rows = (len(badge_paths) + cols - 1) // cols  # ceiling division

    canvas_w = cols * badge_w + (cols + 1) * padding
    canvas_h = rows * badge_h + (rows + 1) * padding
    canvas = Image.new("RGB", (canvas_w, canvas_h), bg)

    for i, path in enumerate(badge_paths):
        badge = Image.open(path)

        col = i % cols
        row = i // cols

        # --- YOUR CODE HERE ---
        # Calculate the x and y position for this badge based on its
        # row and column, then paste it onto the canvas.
        pass

    return canvas


def save_summary_csv(badge_paths, output_path):
    """Write a CSV listing the cities that appear in the collage."""
    with open(output_path, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=["position", "city", "filename"])
        writer.writeheader()
        for i, path in enumerate(badge_paths):
            filename = os.path.basename(path)
            # Extract city name: "badge_Quebec_City.jpg" -> "Quebec City"
            city_name = filename.replace("badge_", "").replace(".jpg", "")
            city_name = city_name.replace("_", " ")
            writer.writerow(
                {
                    "position": i + 1,
                    "city": city_name,
                    "filename": filename,
                }
            )


# -------------------------------------------------------
# Collect badge paths (sorted alphabetically for a tidy grid)
# -------------------------------------------------------
badge_paths = sorted(
    [
        os.path.join("output", f)
        for f in os.listdir("output")
        if f.startswith("badge_") and f.endswith(".jpg")
    ]
)

if not badge_paths:
    print("No badges found in output/ - run badges.py first!")
else:
    collage = build_collage(badge_paths, COLS, BADGE_W, BADGE_H, PADDING, BG_COLOUR)
    collage.save("output/collage.jpg")
    print(
        f"Collage saved: {collage.size[0]}x{collage.size[1]} pixels, "
        f"{len(badge_paths)} badges"
    )

    save_summary_csv(badge_paths, "output/collage_summary.csv")
    print("Summary CSV saved to output/collage_summary.csv")
