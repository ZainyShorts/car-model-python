import csv

# Function to read the values of a specific column from a CSV file
def read_column_values_from_csv(filename, column_name):
    values = []
    with open(filename, 'r', newline='') as file:
        reader = csv.DictReader(file)
        for row in reader:
            if column_name in row:
                values.append(row[column_name])
    return values

# Path to the CSV file
file_path = 'updatedCars.csv'  # Replace 'your_file.csv' with the actual path to your CSV file

# Column name (e.g., "Title")
column_name = 'title'  # Replace 'Title' with the actual column name from your CSV file

# Read the values of the specified column from the CSV file
column_values = read_column_values_from_csv(file_path, column_name)

# Print the values of the specified column
print(f"Values of '{column_name}' column:")
for value in column_values:
    print(value)
