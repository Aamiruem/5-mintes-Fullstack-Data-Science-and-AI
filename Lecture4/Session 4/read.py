import csv

# Write CSV
with open("emp.csv","w",newline="") as f:
    wr = csv.writer(f)
    wr.writerow(["Name","Age"])
    wr.writerow(["Aamir",21])

# Read CSV
with open("emp.csv") as f:
    rd = csv.reader(f)
    for row in rd:
        print(row)

