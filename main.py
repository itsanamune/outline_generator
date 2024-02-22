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

def create_outlines_from_template(template, games):
    """Creates a complete outline for each game, replacing placeholders with the game name."""
    outlines = []
    for game in games:
        updated_outline = template.replace("{game}", game)
        outlines.append({'Outline': updated_outline, 'Game Name': game})
    
    outlines_df = pd.DataFrame(outlines)
    outlines_df.to_excel("OutputFiles/game_outlines.xlsx", index=False, columns=['Outline'])

def read_games_from_excel(file_path):
    """Reads game names from an Excel file."""
    df = pd.read_excel(file_path)  # Corrected from pd.read.read_games_from_excel to pd.read_excel
    games = df.iloc[:, 0].tolist()
    return games


input_dir = 'InputFiles'
template_file_path = find_first_file(input_dir, '.txt') # Changed to look for .txt files
game_names_file_path = find_first_file(input_dir, '.xlsx')

if template_file_path and game_names_file_path:
    template_outline = read_template_from_text(template_file_path) # Changed function call to read from .txt
    games = read_games_from_excel(game_names_file_path)
    create_outlines_from_template(template_outline, games)
    print("Outlines have been created and saved to game_outlines.xlsx.")
else:
    print("Required files (.txt template or .xlsx with game names) not found in InputFiles directory.")
