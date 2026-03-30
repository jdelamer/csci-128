import csv

# -------------------------------------------------------
# The manual way: open like a text file and split on ','
# -------------------------------------------------------
print("=== Manual reading ===")
with open("data/students.csv", "r") as f:
    for line in f:
        line = line.strip()  # remove trailing newline
        fields = line.split(",")
        print(fields)

# -------------------------------------------------------
# The clean way: use csv.reader
# -------------------------------------------------------
print("\n=== csv.reader ===")
with open("data/students.csv", newline="") as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)

# -------------------------------------------------------
# Print just the header, then count data rows
# -------------------------------------------------------
print("\n=== Header and row count ===")
with open("data/students.csv", newline="") as f:
    reader = csv.reader(f)
    header = next(reader)  # read (and consume) the first row
    print("Columns:", header)
    count = 0
    for row in reader:
        count += 1
    print("Number of data rows:", count)

# -------------------------------------------------------
# Experiment 1: print only the name column (index 0)
# -------------------------------------------------------
print("\n=== Names only ===")
with open("data/students.csv", newline="") as f:
    reader = csv.reader(f)
    next(reader)  # skip header
    for row in reader:
        print(row[0])

# -------------------------------------------------------
# Experiment 2: print only rows where grade == "A"
# -------------------------------------------------------
print("\n=== Grade A students ===")
with open("data/students.csv", newline="") as f:
    reader = csv.reader(f)
    next(reader)
    for row in reader:
        if row[1] == "A":
            print(row)

# -------------------------------------------------------
# Experiment 3: count students from Halifax
# -------------------------------------------------------
print("\n=== Halifax count ===")
halifax_count = 0
with open("data/students.csv", newline="") as f:
    reader = csv.reader(f)
    next(reader)
    for row in reader:
        if row[3] == "Halifax":
            halifax_count += 1
print("Students from Halifax:", halifax_count)
