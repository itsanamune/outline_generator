import os
import pandas as pd

# Get the directory of the script
script_dir = os.path.dirname(os.path.realpath(__file__))

# Setup directories
template_dir = os.path.join(script_dir, 'Templates')
csv_dir = os.path.join(script_dir, 'CSVs')
output_dir = os.path.join(script_dir, 'Outputs')

# Function to find the first file with a specific extension
def find_first_file(directory, extension):
    for file in os.listdir(directory):
        if file.endswith(extension):
            return os.path.join(directory, file)
    return None

# Find the first .txt and .csv files
template_path = find_first_file(template_dir, '.txt')
csv_path = find_first_file(csv_dir, '.csv')

# Ensure template and CSV paths were found
if not template_path or not csv_path:
    print("Template or CSV file not found. Please check the directories.")
    exit()

# Read the template
with open(template_path, 'r', encoding='utf-8') as file:
    template = file.read()

# Read CSV, considering the first row as headers for user guidance only
df = pd.read_csv(csv_path, header=None, skiprows=1)

# Initialize a list to collect outlines
outlines = []

# Process CSV for placeholders and replacements
for _, row in df.iterrows():
    outline = template
    for i in range(0, len(row), 2):
        # Check if there is a pair to process (placeholder and replacement)
        if pd.notnull(row[i]) and i+1 < len(row):
            placeholder = row[i]  # Placeholder text with curly braces
            replacement = row[i+1] if pd.notnull(row[i+1]) else ""  # Corresponding replacement text
            outline = outline.replace(placeholder, replacement)
    outlines.append({'Outline': outline})

# Create DataFrame from the list of outlines using pd.concat
output_df = pd.concat([pd.DataFrame([outline]) for outline in outlines], ignore_index=True)

# Save to Excel
output_file_path = os.path.join(output_dir, "Generated_Outlines.xlsx")
output_df.to_excel(output_file_path, index=False)

print("Content outlines generated successfully.")
