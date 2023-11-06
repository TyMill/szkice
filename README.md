
# Szkice Price Update Project

## Overview
This project contains a script that updates the 'Cena' (price) field in a dataset of sketches ('szkice').
It compares prices between two CSV files and updates them if discrepancies are found.

## Files
- `ECsketch.csv`: Original dataset containing 'Eurokod', 'Nr_szkicu', and 'Cena'.
- `price_to_ec.csv`: Dataset containing updated prices for each 'Nr_szkicu'.
- `ceny_final_szkic.csv`: The output file with updated 'Cena'.
- `szkice.py`: The Python script that performs the price update process.

## How to Run
Ensure you have Python installed on your system. Place the `ECsketch.csv` and `price_to_ec.csv` in the same directory as the script. Run the script using the following command:

```sh
python szkice.py
```

The script will create a `ceny_final_szkic.csv` file with the updated prices.

## Dependencies
- pandas: A Python library for data manipulation and analysis.

Make sure to install all required dependencies by running:

```sh
pip install pandas
```

## Author
[Your Name or Organization]

## License
This project is licensed under the [MIT License](LICENSE).

