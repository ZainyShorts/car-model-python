import pandas as pd

pakWheels_df = pd.read_csv("pakWheels.csv")
updatedCars_df = pd.read_csv("merged_data.csv")


print(pakWheels_df.head(10))
print(updatedCars_df.head(10))


if len(updatedCars_df.columns) == len(pakWheels_df.columns):
    print("The number of columns in merged_df is equal to the number of columns in pakWheels_df.")
else:
    print("The number of columns in merged_df is NOT equal to the number of columns in pakWheels_df.")

column_names = pakWheels_df.columns.tolist()
print(column_names)

column_names = updatedCars_df.columns.tolist()
print(column_names)