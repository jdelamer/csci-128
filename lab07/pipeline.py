import csv

# -------------------------------------------------------
# Helper functions (copy from earlier tasks)
# -------------------------------------------------------


def column_avg(data, col_name):
    """Return the average of a numeric column."""
    total = 0.0
    count = 0
    for row in data:
        total += float(row[col_name])
        count += 1
    if count == 0:
        return 0.0
    return total / count


def column_min(data, col_name):
    """Return the minimum of a numeric column."""
    current_min = float(data[0][col_name])
    for row in data[1:]:
        val = float(row[col_name])
        if val < current_min:
            current_min = val
    return current_min


def column_max(data, col_name):
    """Return the maximum of a numeric column."""
    current_max = float(data[0][col_name])
    for row in data[1:]:
        val = float(row[col_name])
        if val > current_max:
            current_max = val
    return current_max


# -------------------------------------------------------
# Step 1: Load data
# -------------------------------------------------------
with open("data/students.csv", newline="") as f:
    reader = csv.DictReader(f)
    fieldnames = reader.fieldnames
    data = list(reader)

print(f"Loaded {len(data)} students from data/students.csv")

# -------------------------------------------------------
# Step 2: Print overall summary
# -------------------------------------------------------
print("\n=== Overall Summary ===")
print(f"  Total students : {len(data)}")
print(f"  Min score      : {column_min(data, 'score'):.1f}")
print(f"  Max score      : {column_max(data, 'score'):.1f}")
print(f"  Avg score      : {column_avg(data, 'score'):.2f}")

# -------------------------------------------------------
# Step 3: Print students above the class average
# -------------------------------------------------------
avg = column_avg(data, "score")
print(f"\n=== Students above class average ({avg:.2f}) ===")
above_avg = []
for row in data:
    if float(row["score"]) > avg:
        above_avg.append(row)
        print(f"  {row['name']}: {row['score']}")

# -------------------------------------------------------
# Step 4: Group students by city
# -------------------------------------------------------
city_scores = {}  # city -> list of scores
for row in data:
    city = row["city"]
    score = float(row["score"])
    if city not in city_scores:
        city_scores[city] = []
    city_scores[city].append(score)

# -------------------------------------------------------
# Step 5: Print average score per city
# -------------------------------------------------------
print("\n=== Average Score by City ===")
for city, scores in city_scores.items():
    city_avg = sum(scores) / len(scores)
    print(f"  {city}: {city_avg:.2f}  (n={len(scores)})")

# -------------------------------------------------------
# Step 6: Save students above average to a new CSV
# -------------------------------------------------------
with open("data/above_average.csv", "w", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    for row in above_avg:
        writer.writerow(row)

print(f"\nSaved {len(above_avg)} above-average students to data/above_average.csv")
print("Pipeline complete.")
