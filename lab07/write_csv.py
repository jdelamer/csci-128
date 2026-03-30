import csv

# -------------------------------------------------------
# Load the original data
# -------------------------------------------------------
with open("data/students.csv", newline="") as f:
    reader = csv.DictReader(f)
    fieldnames = reader.fieldnames  # remember the column names
    data = list(reader)

# -------------------------------------------------------
# Filter: keep only students with score >= 80
# -------------------------------------------------------
high_achievers = [row for row in data if int(row["score"]) >= 80]

# -------------------------------------------------------
# Write filtered rows to a new CSV
# -------------------------------------------------------
with open("data/high_achievers.csv", "w", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()  # write the column names first
    for row in high_achievers:
        writer.writerow(row)

print("Saved", len(high_achievers), "rows to data/high_achievers.csv")

# -------------------------------------------------------
# Second program: city counts summary CSV
# -------------------------------------------------------

# Count students per city using a dictionary
city_counts = {}
for row in data:
    city = row["city"]
    if city in city_counts:
        city_counts[city] += 1
    else:
        city_counts[city] = 1

# Write the summary to data/city_counts.csv
with open("data/city_counts.csv", "w", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=["city", "count"])
    writer.writeheader()
    for city, count in city_counts.items():
        writer.writerow({"city": city, "count": count})

print("City counts:")
for city, count in city_counts.items():
    print(f"  {city}: {count}")
print("Saved city summary to data/city_counts.csv")

# -------------------------------------------------------
# Experiment 1: write only grade-A students to a CSV
# -------------------------------------------------------
grade_a = [row for row in data if row["grade"] == "A"]
with open("data/grade_a.csv", "w", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    for row in grade_a:
        writer.writerow(row)
print("\nSaved", len(grade_a), "grade-A rows to data/grade_a.csv")

# -------------------------------------------------------
# Experiment 2: add a pass_fail column and save
# -------------------------------------------------------
for row in data:
    row["pass_fail"] = "Pass" if int(row["score"]) >= 60 else "Fail"

extended_fields = list(fieldnames) + ["pass_fail"]
with open("data/students_pf.csv", "w", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=extended_fields)
    writer.writeheader()
    for row in data:
        writer.writerow(row)
print("Saved pass/fail data to data/students_pf.csv")
