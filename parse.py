import csv
import json
import argparse
import os

def csv_to_json(csv_file_path, sort_key):
    try:
        with open(csv_file_path, mode='r', newline='', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            data = list(reader)

        if sort_key not in data[0]:
            return "Error: Invalid sort key. Please use one of the following: name, phone, email, address."

        sorted_data = sorted(data, key=lambda x: x[sort_key])

        # Creating the JSON file name based on the CSV file name
        json_file_path = os.path.splitext(csv_file_path)[0] + '.json'
        with open(json_file_path, 'w', encoding='utf-8') as json_file:
            json.dump(sorted_data, json_file, indent=4)

        return f"JSON file created successfully: {json_file_path}"
    except FileNotFoundError:
        return "Error: File not found. Please check the file path and try again."
    except Exception as e:
        return f"Error: An unexpected error occurred. {str(e)}"

def main():
    # Argument parser setup
    parser = argparse.ArgumentParser(description='Convert CSV to JSON with sorting.')
    parser.add_argument('csv_file', help='Path to the CSV file')
    parser.add_argument('sort_key', help='The field to sort by (name, phone, email, address)')
    args = parser.parse_args()

    # Process the CSV and generate JSON
    result = csv_to_json(args.csv_file, args.sort_key)
    print(result)

if __name__ == "__main__":
    main()
