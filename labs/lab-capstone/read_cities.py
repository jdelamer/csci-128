import csv


def load_cities(filepath):
    """Load cities.csv and return a list of dicts."""
    with open(filepath, newline="") as f:
        # --- YOUR CODE HERE ---
        # Use csv.DictReader to read the file.
        # Return a list of all rows.
        pass


def filter_coastal(cities):
    """Return only the cities where coastal == 'yes'."""
    # --- YOUR CODE HERE ---
    pass


def filter_by_min_population(cities, min_pop):
    """Return cities whose population is >= min_pop."""
    # --- YOUR CODE HERE ---
    pass


def sort_by_population(cities, descending=True):
    """Return cities sorted by population."""
    # --- YOUR CODE HERE ---
    pass


def print_city_table(cities):
    """Print a simple table of city name, country, and population."""
    print(f"{'City':<15} {'Country':<15} {'Population':>12}")
    print("-" * 44)
    for city in cities:
        print(
            f"{city['name']:<15} {city['country']:<15} {int(city['population']):>12,}"
        )


# -------------------------------------------------------
# Main
# -------------------------------------------------------
cities = load_cities("data/cities.csv")

print("=== All cities ===")
print_city_table(cities)

print("\n=== Coastal cities only ===")
print_city_table(filter_coastal(cities))

print("\n=== Cities with population >= 1,000,000 ===")
big_cities = filter_by_min_population(cities, 1_000_000)
print_city_table(sort_by_population(big_cities))
