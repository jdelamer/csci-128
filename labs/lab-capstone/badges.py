import csv

from PIL import Image, ImageDraw, ImageFont

BADGE_W = 300
BADGE_H = 150

# Colour scheme: coastal cities get a blue badge, inland cities get green.
COASTAL_COLOUR = (70, 130, 180)  # steel blue
INLAND_COLOUR = (60, 140, 80)  # forest green
TEXT_COLOUR = (255, 255, 255)  # white


def compute_density(population, area_km2):
    """Return population density rounded to one decimal place."""
    # --- YOUR CODE HERE ---
    pass


def make_badge(city_name, country, density, is_coastal):
    """Return a BADGE_W x BADGE_H PIL Image for one city.

    The badge must show:
      - A filled background (blue for coastal, green for inland)
      - The city name in large text at the top
      - The country name in smaller text below the city name
      - The density (people/km2) at the bottom
    """
    bg_colour = COASTAL_COLOUR if is_coastal else INLAND_COLOUR
    img = Image.new("RGB", (BADGE_W, BADGE_H), bg_colour)
    draw = ImageDraw.Draw(img)

    # --- YOUR CODE HERE ---
    # Draw the city name, country, and density onto the badge.

    return img


# -------------------------------------------------------
# Load data and generate one badge per city
# -------------------------------------------------------
with open("data/cities.csv", newline="") as f:
    cities = list(csv.DictReader(f))

badge_images = []  # collect badges in this list

for city in cities:
    name = city["name"]
    country = city["country"]
    pop = int(city["population"])
    area = float(city["area_km2"])
    coastal = city["coastal"] == "yes"

    density = compute_density(pop, area)
    badge = make_badge(name, country, density, coastal)

    badge.save(f"output/badge_{name.replace(' ', '_')}.jpg")
    badge_images.append(badge)
    print(f"Badge created: {name}")

print(f"\n{len(badge_images)} badges saved to output/")
