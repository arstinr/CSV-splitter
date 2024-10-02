import csv
import os
import logging
from typing import List, Dict

# Set the maximum rows per file directly in the script
MAX_ROWS_PER_FILE = 100000  # Adjust this value as needed
INPUT_DIR = "input_csvs"
OUTPUT_DIR = "output_csvs"

def split_csv(input_file: str) -> None:
    base_name = os.path.splitext(os.path.basename(input_file))[0]
    file_output_dir = os.path.join(OUTPUT_DIR, base_name)
    os.makedirs(file_output_dir, exist_ok=True)
    
    with open(input_file, 'r', newline='') as csvfile:
        reader = csv.reader(csvfile)
        headers = next(reader)
        
        row_count = 0
        file_count = 0
        current_writer = None
        current_output = None
        
        for row in reader:
            if row_count % MAX_ROWS_PER_FILE == 0:
                if current_output:
                    current_output.close()
                
                file_count += 1
                output_file = os.path.join(file_output_dir, f"{base_name}_part{file_count}.csv")
                current_output = open(output_file, 'w', newline='')
                current_writer = csv.writer(current_output)
                current_writer.writerow(headers)
            
            current_writer.writerow(row)
            row_count += 1
        
        if current_output:
            current_output.close()
    
    logging.info(f"Split {input_file} into {file_count} files in {file_output_dir}")

def main() -> None:
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
    
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    
    csv_files = [f for f in os.listdir(INPUT_DIR) if f.endswith('.csv')]
    
    for csv_file in csv_files:
        input_path = os.path.join(INPUT_DIR, csv_file)
        logging.info(f"Processing {input_path}")
        split_csv(input_path)
    
    logging.info("All CSV files have been processed")

if __name__ == "__main__":
    main()
