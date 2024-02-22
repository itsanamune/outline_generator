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

def create_outlines_from_template(template, data):
    outlines = []
    for item in data:
        updated_outline = template
        for placeholder, replacement in item.items():
            updated_outline = updated_outline.replace(f"{{{placeholder}}}", replacement)
        outlines.append({'Outline': updated_outline, 'Game Name': item.get('game', 'N/A')})
    
    outlines_df = pd.DataFrame(outlines)
    outlines_df.to_excel("OutputFiles/game_outlines.xlsx", index=False)


def read_data_from_excel(file_path):
    df = pd.read_excel(file_path)
    data = []
    placeholders = df.columns.tolist()
    for index, row in df.iterrows():
        replacements = row.tolist()
        data.append(dict(zip(placeholders, replacements)))
    return data


input_dir = 'InputFiles'
template_file_path = find_first_file(input_dir, '.txt') # Changed to look for .txt files
game_names_file_path = find_first_file(input_dir, '.xlsx')

if template_file_path and game_names_file_path:
    template_outline = read_template_from_text(template_file_path) # Continue using this line as is
    data = read_data_from_excel(game_names_file_path)  # Updated to use read_data_from_excel
    create_outlines_from_template(template_outline, data)  # Correctly using the updated data variable
    print("Outlines have been created and saved to game_outlines.xlsx.")
else:
    print("Required files (.txt template or .xlsx with game names) not found in InputFiles directory.")

