import pandas as pd

# Path to your .dat file
file_path = 'D:/Computer Aplication/WorkPlacement/Projects/Project4/NRCAN_Laurentian_Basin/Export/Seis/20.dat'

df = pd.read_csv(file_path, delim_whitespace=True)

# Display the first few rows of the DataFrame to verify the data
# print(df.head())

# Save the DataFrame to a CSV file
output_csv_path = 'D:/Computer Aplication/WorkPlacement/Projects/Project4/NRCAN_Laurentian_Basin/Export/Seis/output.csv'
df.to_csv(output_csv_path, index=False)

print(f'Data has been successfully saved to {output_csv_path}')
