import pandas as pd
import json
import csv

# Load the JSON file
with open('2_ProjectFinder.json', encoding='utf-8-sig') as f:
    data = json.load(f)

# Flatten the JSON structure, converting lists to strings
flattened_data = [{key: ' '.join(value) if isinstance(value, list) else value for key, value in item.items()} for item in data]

# Create a DataFrame from the flattened JSON data
df = pd.DataFrame(flattened_data)

# Write the DataFrame to a CSV file with ";" as a delimiter
# Ensure that values containing ";" are properly quoted, THIS COULD BE A SOURCE FOR ERRORS. KEEP AN EYE ON THIS
df.to_csv('3_ProjectFinder.csv', sep=';', index=False, encoding='utf-8-sig', quoting=csv.QUOTE_MINIMAL)

print("Conversion completed. The CSV file has been saved as 'output.csv'")
