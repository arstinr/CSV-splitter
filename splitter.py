import csv
import os
import argparse
import logging
from typing import List, Dict

MAX_ROWS_PER_FILE = 1000000  # Adjust as needed
INPUT_DIR = "input_csvs"
OUTPUT_DIR = "output_csvs"

def split_csv(input_file: str) -> None:
    base_name = os.path.splitext(os.path.basename(input_file))[0]
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    
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
                output_file = os.path.join(OUTPUT_DIR, f"{base_name}_part{file_count}.csv")
                current_output = open(output_file, 'w', newline='')
                current_writer = csv.writer(current_output)
                current_writer.writerow(headers)
            
            current_writer.writerow(row)
            row_count += 1
        
        if current_output:
            current_output.close()
    
    logging.info(f"Split {input_file} into {file_count} files")

def main() -> None:
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
    
    parser = argparse.ArgumentParser(description="Split large CSV files into smaller ones")
    parser.add_argument("--input-dir", default=INPUT_DIR, help="Input directory containing CSV files")
    parser.add_argument("--output-dir", default=OUTPUT_DIR, help="Output directory for split CSV files")
    parser.add_argument("--max-rows", type=int, default=MAX_ROWS_PER_FILE, help="Maximum rows per output file")
    args = parser.parse_args()
    
    global INPUT_DIR, OUTPUT_DIR, MAX_ROWS_PER_FILE
    INPUT_DIR = args.input_dir
    OUTPUT_DIR = args.output_dir
    MAX_ROWS_PER_FILE = args.max_rows
    
    csv_files = [f for f in os.listdir(INPUT_DIR) if f.endswith('.csv')]
    
    for csv_file in csv_files:
        input_path = os.path.join(INPUT_DIR, csv_file)
        logging.info(f"Processing {input_path}")
        split_csv(input_path)
    
    logging.info("All CSV files have been processed")

if __name__ == "__main__":
    main()
