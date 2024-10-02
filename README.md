# CSV Splitter

*Note: This code was built with assistance from CursorAI.*

## Description

This Python script splits large CSV files into smaller, more manageable files. It's particularly useful for preparing large datasets for upload to services like Google Sheets, which have row limitations.

## Features

- Automatically processes all CSV files in the input directory
- Creates separate output folders for each input file
- Configurable maximum rows per output file
- Preserves headers in each split file

## Requirements

- Python 3.6 or higher

## Setup

1. Clone this repository or download the `splitter.py` file.
2. Ensure you have a directory named `input_csvs` in the same location as the `splitter.py` file.

## Usage

1. Place your large CSV files in the `input_csvs` directory.

2. (Optional) Open `splitter.py` and adjust the `MAX_ROWS_PER_FILE` constant if you want to change the maximum number of rows per output file. By default, it's set to 1,000,000 rows.

3. Run the script:
   ```
   python splitter.py
   ```

4. The script will process all CSV files in the `input_csvs` directory and create split files in separate folders within the `output_csvs` directory.

## Output

The script creates an `output_csvs` directory with the following structure:

```
output_csvs/
├── original_file1_name/
│   ├── original_file1_name_part1.csv
│   ├── original_file1_name_part2.csv
│   └── ...
└── original_file2_name/
    ├── original_file2_name_part1.csv
    ├── original_file2_name_part2.csv
    └── ...
```

Each input file gets its own subdirectory in `output_csvs`, containing the split CSV files.

## Notes

- The script automatically skips non-CSV files in the input directory.
- If a file with the same name already exists in the output directory, it will be overwritten.
- The script uses Python's built-in `csv` module, which should handle most standard CSV formats.

## Troubleshooting

If you encounter any issues:

1. Ensure you have Python 3.6 or higher installed.
2. Check that your input CSV files are not corrupted and are properly formatted.
3. Make sure you have write permissions in the directory where the script is located.

For any other issues, please open an issue in the GitHub repository.
