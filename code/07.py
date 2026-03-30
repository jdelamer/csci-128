import csv

with open("students.csv", "r") as f:
    lines = f.readlines()

# header = lines[0].strip().split(",")
# print("Header:", header)
# print(lines[1:])


# line = "Alice,A,92\n\n\n".strip().split(",")
# print(line)


data = []
for line in lines[1:]:
    line = line.strip()
    if line == "":
        continue
    row = line.split(",")
    data.append(row)

# print(data)

# for row in data:
#     name  = row[0]
#     grade = row[1]
#     score = int(row[2])
#     print(name, "got a", grade, "with score", score)


# csv.reader handles commas, quotes, and newlines for us
# with open("students.csv", "r") as f:
    # reader = csv.reader(f)

    # header = next(reader)       # read the first row as header
    # print("Columns:", header)   # Columns: ['Name', 'Grade', 'Score']

    # data = []
    # for row in reader:          # each row is already a list
    #     data.append(row)

    # print(data)


# with open("students.csv", "r", newline="") as f:
#     reader = csv.DictReader(f)  # uses first row as keys

#     data = []
#     for row in reader:
#         data.append(row)  # each row is a dictionary

# print(data)
# Each row is now a dict: {'Name': ..., 'Grade': ..., 'Score': ...}
# for row in data:
#     name = row["Name"]  # no need to remember column 0
#     grade = row["Grade"]  # no need to remember column 1
#     score = float(row["Score"])  # convert string to number
#     print(f"{name}: {grade} ({score})")


with open("students.csv", "r", newline="") as f:
    reader = csv.DictReader(f)
    data = list(reader)

# # ---- find max score ----
current_max = float(data[0]["Score"])   # start with first value
max_student = data[0]["Name"]

for row in data:
    score = float(row["Score"])
    if score > current_max:
        current_max = score
        max_student = row["Name"]

print("Highest score:", current_max, "by", max_student)

# with open("students.csv", "r", newline="") as f:
#     reader = csv.DictReader(f)
#     data = list(reader)

# total = 0.0
# count = 0

# for row in data:
#     total = total + float(row["Score"])
#     count = count + 1


# if count > 0:              # Guard against empty files
#     average = total / count
#     print(f"Average score: {average:.2f}")
# else:
#     print("No data found.")

# with open("students.csv", "r", newline="") as f:
#     data = list(csv.DictReader(f))
# passing = []
# for row in data:
#     score = float(row["Score"])   # convert string -> number first!
#     if score >= 80:
#         passing.append(row)

# for row in passing:
#     print(f"  {row['Name']:10s}  {row['Score']}")
#
# with open("students.csv", "r", newline="") as f:
#     data = list(csv.DictReader(f))
# a_students = []
# for row in data:
#     if row["Grade"] == "A":       # string comparison, no conversion needed
#         a_students.append(row)
# print(f"A-grade students ({len(a_students)} found):")
# for row in a_students:
#     print(f"  {row['Name']}")

# with open("students.csv", "r", newline="") as f:
#     data = list(csv.DictReader(f))

# # Sort by Score, highest first
# by_score = sorted(data, key=lambda row: float(row["Score"]),reverse=True)

# print("Ranked by score:")
# for i, row in enumerate(by_score):
#     print(f"  {i+1}. {row['Name']:10s} {row['Score']}")

# # Sort alphabetically by Name (ascending)
# by_name = sorted(data, key=lambda row: row["Name"])

# print("\nAlphabetical order:")
# for row in by_name:
#     print(f"  {row['Name']}")

# with open("output.csv", "w", newline="") as f:
#     writer = csv.writer(f)
#     for row in results:
#         writer.writerow(row)

# # You can also write all rows at once:
# with open("output2.csv", "w", newline="") as f:
#     writer = csv.writer(f)
#     writer.writerows(results)   # note: writerows (plural)
