
# Project Overview

This Python project automates the creation of game outlines by utilizing a template and game-specific data from a CSV file. It reads a template from a text file and game data from a CSV file, replaces placeholders in the template with actual data, and then saves the customized outlines to an Excel file. This automation streamlines the process of generating game outlines, making it efficient and scalable.

## Installation

To set up your environment to run this script, follow these steps:

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/itsanamune/outline_generator.git
   ```
2. **Create a Virtual Environment:**
   Before installing dependencies, it's recommended to create a virtual environment to avoid conflicts with other projects.
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```
3. **Install Dependencies:**
   This project requires `pandas` for data manipulation and Excel file generation.
   ```bash
   pip install pandas
   ```

## Usage

To use this script, you need to have a `.txt` template file and a `.csv` file with placeholder-replacement pairs in the `InputFiles` directory. Then, execute the script with:

```bash
python main.py
```

The script will generate an Excel file named `game_outlines.xlsx` in the `OutputFiles` directory, containing the customized outlines for each game.

### Directory Structure

Ensure the following directory structure:

- `InputFiles/`: Contains the template `.txt` file and the `.csv` file with data.
- `OutputFiles/`: The script saves the generated Excel file here.

## Contributing

Contributions are welcome! If you have suggestions for improving this script, feel free to open an issue or submit a pull request.

## License

Specify the license under which this project is available, such as MIT, GPL, etc.

This README template provides a basic structure. Depending on the project's complexity and specific requirements, additional sections such as 'Running Tests', 'Deployment', and 'Acknowledgments' may be included to provide a comprehensive overview.
