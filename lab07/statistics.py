import csv


def column_min(data, col_name):
    """Return the minimum numeric value in a named column.

    Parameters
    ----------
    data : list of dict
        Rows loaded from a CSV file (e.g. via csv.DictReader).
    col_name : str
        The name of the column to inspect.

    Returns
    -------
    float
        The smallest value found in that column.
    """
    # Step 1: Start with the first row's value as the current minimum
    current_min = float(data[0][col_name])
    # Step 2: Loop through the remaining rows
    for row in data[1:]:
        value = float(row[col_name])
        # Step 3: If this value is smaller, update the minimum
        if value < current_min:
            current_min = value
    # Step 4: Return the minimum
    return current_min


def column_max(data, col_name):
    """Return the maximum numeric value in a named column.

    Parameters
    ----------
    data : list of dict
        Rows loaded from a CSV file.
    col_name : str
        The name of the column to inspect.

    Returns
    -------
    float
        The largest value found in that column.
    """
    # Similar to column_min but track the maximum instead
    current_max = float(data[0][col_name])
    for row in data[1:]:
        value = float(row[col_name])
        if value > current_max:
            current_max = value
    return current_max


def column_avg(data, col_name):
    """Return the average (mean) of a numeric column.

    Parameters
    ----------
    data : list of dict
        Rows loaded from a CSV file.
    col_name : str
        The name of the column to average.

    Returns
    -------
    float
        The mean value, or 0.0 if data is empty.
    """
    # Step 1: Initialise running total and a counter
    total = 0.0
    count = 0
    # Step 2: Loop through every row
    for row in data:
        # Step 3: Add the converted value and increment the counter
        total += float(row[col_name])
        count += 1
    # Step 4: Return the average; guard against an empty dataset
    if count == 0:
        return 0.0
    return total / count


# -------------------------------------------------------
# Test code: load the data, call all three functions
# -------------------------------------------------------
with open("data/students.csv", newline="") as f:
    data = list(csv.DictReader(f))

print("=== Score Statistics ===")
print(f"  Min score : {column_min(data, 'score'):.1f}")
print(f"  Max score : {column_max(data, 'score'):.1f}")
print(f"  Avg score : {column_avg(data, 'score'):.2f}")

# -------------------------------------------------------
# Experiment 1: stats for each grade group separately
# -------------------------------------------------------
print("\n=== Stats by grade ===")
for grade in ["A", "B", "C"]:
    group = [row for row in data if row["grade"] == grade]
    if group:
        print(
            f"  Grade {grade}: "
            f"min={column_min(group, 'score'):.1f}  "
            f"max={column_max(group, 'score'):.1f}  "
            f"avg={column_avg(group, 'score'):.2f}"
        )

# -------------------------------------------------------
# Experiment 2: what happens with a non-numeric column?
# Try: column_min(data, 'name')
# Uncomment the line below and run to see the error.
# -------------------------------------------------------
# print(column_min(data, "name"))
