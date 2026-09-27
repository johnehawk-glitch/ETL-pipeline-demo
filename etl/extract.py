import csv

def extract_data(path="data/input.csv"):
    rows = []
    with open(path, newline='') as f:
        reader = csv.DictReader(f)
        for row in reader:
            rows.append(row)
    # These changes are to test Feature Extract branch
    # This is a second change to Feature Extract branch
    return rows
