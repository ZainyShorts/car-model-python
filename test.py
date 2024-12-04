import csv

# Function to read the values in the "Name" column of a CSV file
def read_names_from_csv(filename,column):
    names = []
    with open(filename, 'r', newline='') as file:
        reader = csv.DictReader(file)
        for row in reader:
            names.append(row[column])
    return names

# Function to read the column headers (titles) of a CSV file
def read_titles_from_csv(filename):
    with open(filename, 'r', newline='') as file:
        reader = csv.reader(file)
        titles = next(reader)  # Read the first row (header)
    return titles

# Paths to the CSV files
file1_path = 'pakWheels.csv'
file2_path = 'updatedCars.csv'

# Read the values in the "Name" column of the first CSV file
names_from_file1 = read_names_from_csv(file1_path,'Name')

# Read the column headers (titles) of the second CSV file
titles_from_file2 = read_titles_from_csv(file2_path,'title')

# Compare each name from file1 with the titles from file2
for name in names_from_file1:
    if name in titles_from_file2:
        print(name)
