import pandas as pd

# Specify the path to your Excel file
excel_file_path = 'sample.xlsx'

# Read the Excel file into a DataFrame
df = pd.read_excel(excel_file_path)

# Display the contents of the DataFrame
print(df)
