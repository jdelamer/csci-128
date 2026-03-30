import csv


def filter_rows(data, col_name, value):
    """Return only rows where col_name exactly equals value.

    Parameters
    ----------
    data : list of dict
        The full dataset.
    col_name : str
        Column to test.
    value : str
        The exact string value to match.

    Returns
    -------
    list of dict
        A new list containing only the matching rows.
    """
    # Step 1: Create an empty result list
    result = []
    # Step 2: Loop through each row
    for row in data:
        # Step 3: If the column matches, keep the row
        if row[col_name] == value:
            result.append(row)
    # Step 4: Return the filtered list
    return result


def filter_rows_above(data, col_name, threshold):
    """Return rows where the numeric column value is strictly above threshold.

    Parameters
    ----------
    data : list of dict
        The full dataset.
    col_name : str
        The numeric column to test.
    threshold : float
        Keep rows whose value is greater than this number.

    Returns
    -------
    list of dict
        A new list containing only the matching rows.
    """
    # Similar to filter_rows but convert to float and compare numerically
    result = []
    for row in data:
        if float(row[col_name]) > threshold:
            result.append(row)
    return result


def filter_rows_between(data, col_name, low, high):
    """Return rows where low <= numeric value <= high.

    Parameters
    ----------
    data : list of dict
        The full dataset.
    col_name : str
        The numeric column to test.
    low : float
        Inclusive lower bound.
    high : float
        Inclusive upper bound.

    Returns
    -------
    list of dict
        Rows whose column value falls within [low, high].
    """
    result = []
    for row in data:
        val = float(row[col_name])
        if low <= val <= high:
            result.append(row)
    return result


# -------------------------------------------------------
# Load dataset
# -------------------------------------------------------
with open("data/students.csv", newline="") as f:
    data = list(csv.DictReader(f))

# Filter for Halifax students
print("=== Halifax students ===")
halifax = filter_rows(data, "city", "Halifax")
for row in halifax:
    print(" ", row["name"])

# Filter for score above 80
print("\n=== Score above 80 ===")
high_scores = filter_rows_above(data, "score", 80)
for row in high_scores:
    print(f"  {row['name']}: {row['score']}")

# -------------------------------------------------------
# Experiment 1: students from Truro with score above 70
# -------------------------------------------------------
print("\n=== Truro students with score > 70 ===")
truro = filter_rows(data, "city", "Truro")
truro_above_70 = filter_rows_above(truro, "score", 70)
for row in truro_above_70:
    print(f"  {row['name']}: {row['score']}")

# -------------------------------------------------------
# Experiment 2: students with grade B or C
# -------------------------------------------------------
print("\n=== Grade B or C students ===")
b_or_c = []
for row in data:
    if row["grade"] == "B" or row["grade"] == "C":
        b_or_c.append(row)
for row in b_or_c:
    print(f"  {row['name']}: grade {row['grade']}, score {row['score']}")
