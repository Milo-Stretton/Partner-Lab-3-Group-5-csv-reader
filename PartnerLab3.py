# CIS-117 Lab3
# This program reads country_full.csv and creates separate
# CSV files for each region, containing only country names
# and their corresponding regions.
#
# Group 5
# Jesus Rios and Milo Stretton
# Milo: Worked on reading the input CSV file.
# Jesus: Worked on writing the regional CSV files.

import csv
from pathlib import Path

try:
    regions = {}

    # Reading portion - Milo Stretton
    with open(Path(__file__).with_name("country_full.csv"),
              "r", newline="", encoding="utf-8-sig") as f:

        csv_reader = csv.reader(f)
        next(csv_reader)

        for items in csv_reader:
            country = items[0]
            region = items[5]

            if region == "":
                region = "Unknown"

            if region not in regions:
                regions[region] = []

            regions[region].append([country, region])

    # Writing portion - Jesus Rios
    for region, countries in regions.items():

        filename = region + ".csv"

        with open(Path(__file__).with_name(filename),
                  "w", newline="", encoding="utf-8") as output_file:

            csv_writer = csv.writer(output_file)

            csv_writer.writerow(["Country", "Region"])
            csv_writer.writerows(countries)

        print(filename, "created successfully!")

except FileNotFoundError:
    print("Error: File not found.")

except PermissionError:
    print("Error: Permission denied.")

except IOError:
    print("Error: Input/Output error.")

except (IndexError, csv.Error) as error:
    print("Error processing CSV:", error)

