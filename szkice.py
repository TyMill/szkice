
import pandas as pd

# Read the ECsketch.csv file
ec_sketch_data = pd.read_csv('ECsketch.csv', delimiter=';')

# Extract unique Nr_szkicu and Cena from ECsketch.csv
unique_sketch_data = ec_sketch_data[['Nr_szkicu', 'Cena']].drop_duplicates()

# Read the price_to_ec.csv file
price_data = pd.read_csv('price_to_ec.csv', delimiter=';')
unique_price_data = price_data[['Nr_szkicu', 'Cena']].drop_duplicates()

# Create a dictionary for quick look-up of prices from price_to_ec
price_dict = dict(zip(unique_price_data.Nr_szkicu, unique_price_data.Cena))

# Update Cena in ec_sketch_data if it's different in price_to_ec
for index, row in unique_sketch_data.iterrows():
    nr_szkicu = row['Nr_szkicu']
    if nr_szkicu in price_dict and row['Cena'] != price_dict[nr_szkicu]:
        unique_sketch_data.at[index, 'Cena'] = price_dict[nr_szkicu]

# Save the final DataFrame to a new CSV file
unique_sketch_data.to_csv('ceny_final_szkic.csv', index=False, sep=';')
