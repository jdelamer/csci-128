import csv

# -------------------------------------------------------
# Load with DictReader and print name + score
# -------------------------------------------------------
print("=== All students (name, score) ===")
with open("data/students.csv", newline="") as f:
    reader = csv.DictReader(f)
    for row in reader:
        print(row["name"], "->", row["score"])

# -------------------------------------------------------
# Print only students with score > 80
# -------------------------------------------------------
print("\n=== Score > 80 ===")
with open("data/students.csv", newline="") as f:
    reader = csv.DictReader(f)
    for row in reader:
        if int(row["score"]) > 80:
            print(row["name"], row["score"])

# -------------------------------------------------------
# Find the student with the highest score
# -------------------------------------------------------
print("\n=== Highest scorer ===")
with open("data/students.csv", newline="") as f:
    reader = csv.DictReader(f)
    best_name = ""
    best_score = -1
    for row in reader:
        current_score = int(row["score"])
        if current_score > best_score:
            best_score = current_score
            best_name = row["name"]
print("Top student:", best_name, "with score", best_score)

# -------------------------------------------------------
# Experiment 1: print names sorted alphabetically
# -------------------------------------------------------
print("\n=== Alphabetical names ===")
with open("data/students.csv", newline="") as f:
    reader = csv.DictReader(f)
    names = [row["name"] for row in reader]
print(sorted(names))

# -------------------------------------------------------
# Experiment 2: count students per grade
# -------------------------------------------------------
print("\n=== Students per grade ===")
grade_counts = {"A": 0, "B": 0, "C": 0}
with open("data/students.csv", newline="") as f:
    reader = csv.DictReader(f)
    for row in reader:
        grade = row["grade"]
        if grade in grade_counts:
            grade_counts[grade] += 1
for grade, count in grade_counts.items():
    print(f"  Grade {grade}: {count} student(s)")

# -------------------------------------------------------
# Experiment 3: student with the lowest score
# -------------------------------------------------------
print("\n=== Lowest scorer ===")
with open("data/students.csv", newline="") as f:
    reader = csv.DictReader(f)
    worst_name = ""
    worst_score = 9999
    for row in reader:
        current_score = int(row["score"])
        if current_score < worst_score:
            worst_score = current_score
            worst_name = row["name"]
print("Lowest student:", worst_name, "with score", worst_score)
