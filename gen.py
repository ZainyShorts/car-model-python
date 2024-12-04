import pandas as pd


pakWheels = pd.read_csv('pakWheels.csv',usecols=["Model Year"])
updatedCars = pd.read_csv('updatedCars.csv',usecols=["model_year"])

for index, (pakWheel_row, updatedCar_row) in enumerate(zip(pakWheels.values, updatedCars.values)):
    pakWheel_Name = pakWheel_row[0]  # Get the value from the "Name" column in pakWheels
    updatedCar_title = updatedCar_row[0]  # Get the value from the "title" column in updatedCars
    
    # Check if the value in the "Name" column matches the value in the "title" column
    if pakWheel_Name == updatedCar_title:
        # Print the entire row from pakWheels if the values match
        print("Matching Row from pakWheels:")
        print(pakWheels.iloc[index])
        print()
