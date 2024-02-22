import pandas as pd
import os

def find_first_file(directory, extension):
    """Finds the first file in the specified directory with the given extension."""
    for file in os.listdir(directory):
        if file.endswith(extension):
            return os.path.join(directory, file)
    return None

def read_template_from_text(file_path):
    """Reads the entire template from a text file and returns it as a single string."""
    with open(file_path, 'r', encoding='utf-8') as file:
        full_text = file.read()
    return full_text

def read_placeholder_replacements(file_path):
    """Reads the placeholder-replacement pairs from a CSV file."""
    return pd.read_csv(file_path)

def create_outlines_from_template(template, replacements_df):
    """Creates a complete outline for each game, replacing all placeholders."""
    outlines = []
    for index, row in replacements_df.iterrows():
        updated_outline = template
        for placeholder, replacement in row.iteritems():
            if placeholder != 'GameName':  # Skip the GameName column
                updated_outline = updated_outline.replace(placeholder, replacement)
        outlines.append({'Outline': updated_outline, 'Game Name': row['GameName']})
    
    outlines_df = pd.DataFrame(outlines)
    outlines_df.to_excel("OutputFiles/game_outlines.xlsx", index=False)

input_dir = 'InputFiles'
template_file_path = find_first_file(input_dir, '.txt')
replacements_file_path = find_first_file(input_dir, '.csv')  # Assuming the replacements are in a CSV file

if template_file_path and replacements_file_path:
    template_outline = read_template_from_text(template_file_path)
    replacements_df = read_placeholder_replacements(replacements_file_path)
    create_outlines_from_template(template_outline, replacements_df)
    print("Outlines have been created and saved to game_outlines.xlsx.")
else:
    print("Required files (.txt template or .csv with replacements) not found in InputFiles directory.")
