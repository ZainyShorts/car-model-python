import pandas as pd

pakWheels_df = pd.read_csv("pakWheels.csv")
updatedCars_df = pd.read_csv("updatedCars.csv")

for index, row in pakWheels_df.iterrows():
    for index2, row2 in updatedCars_df.iterrows():
        if row['Name'] == row2['title'] and row['Model Year'] == row2['model_year']:
            pakWheels_df.at[index, 'Price'] = row2['price']
            print(row,row2)
            break

pakWheels_df.to_csv("merged_data.csv", index=False)

print("Merged data saved to merged_data.csv")
