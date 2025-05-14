import csv

def read_csv_data(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8', newline='') as csvfile:
            reader = csv.reader(csvfile)
            header = next(reader)
            yield header
            for row in reader:
                yield row
    except FileNotFoundError:
        print(f"Error: file not found in {file_path}")
        yield None
    except Exception as e:
        print(f"Error reading file {file_path}: {e}")
        yield None