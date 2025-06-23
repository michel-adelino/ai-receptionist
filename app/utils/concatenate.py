import pandas as pd
import os

# Step 1: Read the CSV file into a DataFrame
csv_file_path = './data/Clean_System_Scrape2.csv'  # Replace with the actual path to your CSV file
df = pd.read_csv(csv_file_path, encoding='mac_roman')

# Step 2: Use the lambda function to concatenate every third column
# Define a lambda function to concatenate the data in every third column
concat_func = lambda x: ' '.join(str(cell) for cell in x)
# Apply the lambda function to every third column and create a new DataFrame
concatenated_series = df.iloc[:, 2::3].apply(concat_func, axis=0)

concatenated_df = pd.DataFrame(concatenated_series, columns=['Concatenated Data'])

output_csv_path = os.path.join(os.path.expanduser('~'), 'Documents', 'concatenated_data.csv')
concatenated_df.to_csv(output_csv_path, index=False)