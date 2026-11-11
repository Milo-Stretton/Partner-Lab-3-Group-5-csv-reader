import csv
from pathlib import Path
with open(Path(__file__).with_name("country_full.csv"), 'r') as f:
    try:
        csv_reader = csv.reader(f)
        for rows in f:
            items = rows.split(",")
            print(f"{items[0]}, {items[5]}")
    except IOError:
        print("Input/Output error")
    except FileNotFoundError:
        print("File not found error")
    except PermissionError:
        print("Permission error")
    except:
        print("Other error")