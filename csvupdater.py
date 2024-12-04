import pandas as pd

source_df = pd.read_csv('updatedCars.csv')
target_df = pd.read_csv('pakWheels.csv')

updated_df = target_df.copy()

for index, row in source_df.iterrows():
    matching_row = updated_df[(updated_df['Name'] == row['Name']) & (updated_df['ModelYear'] == row['ModelYear'])]
    if not matching_row.empty:
        updated_df.loc[matching_row.index, 'price'] = row['price']

# Write updated DataFrame to a new CSV file
updated_df.to_csv('car.csv', index=False)