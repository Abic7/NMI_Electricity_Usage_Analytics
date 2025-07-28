import csv
import os

# File paths
input_csv_path = "C:/Users/<YourUsername>/Documents/your_raw_energy_data.csv"  # Replace with your input path/filename
formatted_csv_path = "C:/Users/<YourUsername>/Documents/your_formatted_energy_data.csv" # Replace with your output path/filename
row300_output_path = "C:/Users/<YourUsername>/Documents/your_300_energy_data.csv" # Replace with your input path/filename

# Define headers by Row Type
headers = {
    "100": [
        "Row Type", "File Type", "File Creation Date & Time",
        "Meter Data Provider", "Current Retailer"
    ],
    "200": [
        "Row Type", "Your NMI", "Available NMI Suffixes", "Register ID",
        "NMI Suffix Associated", "Meter Number", "Unit Measured",
        "Interval Period", "Next Scheduled Read Date"
    ],
    "300": [
        "Row Type", "Date of Data"
    ] + [f"Interval_{i+1}" for i in range(48)] + [
        "Data Quality Flag", "Reason Code", "Reason Description",
        "Updated Date & Time", "Upload Date & Time"
    ],
    "400": [
        "Row Type", "Starting Interval", "Ending Interval", "Quality Flag",
        "Reason Code", "Reason Description", "Transaction Code",
        "Retailer Service Order", "Read Date & Time", "Index Read"
    ],
    "900": ["Row Type"]  # End of data
}

# Ensure the output directory exists
output_dir = os.path.dirname(formatted_csv_path)
os.makedirs(output_dir, exist_ok=True)

# Utility: Convert YYYYMMDD → YYYY/MM/DD
def format_date(yyyymmdd):
    if len(yyyymmdd) == 8 and yyyymmdd.isdigit():
        return f"{yyyymmdd[:4]}/{yyyymmdd[4:6]}/{yyyymmdd[6:]}"
    return yyyymmdd

# Utility: Convert YYYYMMDDHHMMSS → YYYY/MM/DD HH:MM:SS
def format_datetime(datetime_str):
    if len(datetime_str) == 14 and datetime_str.isdigit():
        return f"{datetime_str[:4]}/{datetime_str[4:6]}/{datetime_str[6:8]} " \
               f"{datetime_str[8:10]}:{datetime_str[10:12]}:{datetime_str[12:]}"
    return datetime_str

# Write formatted output with headers and collect row_type 300 data
row300_data = []

with open(input_csv_path, "r") as infile, open(formatted_csv_path, "w", newline='') as outfile:
    reader = csv.reader(infile)
    writer = csv.writer(outfile)

    for row in reader:
        if not row:
            continue

        row_type = row[0].strip()

        if row_type in headers:
            writer.writerow(headers[row_type])  # Write header

            if row_type == "300":
                # Normalize row length
                data_row = row[:2 + 48] + row[2 + 48:]
                data_row += [""] * (len(headers["300"]) - len(data_row))

                # Format relevant columns
                data_row[1] = format_date(data_row[1].strip())       # Date of Data
                data_row[52] = format_datetime(data_row[52].strip()) # Updated Date & Time
                data_row[53] = format_datetime(data_row[53].strip()) # Upload Date & Time

                writer.writerow(data_row)
                row300_data.append(data_row)

            elif row_type == "400":
                data_row = row + [""] * (len(headers["400"]) - len(row))
                writer.writerow(data_row)

            else:
                writer.writerow(row)

# Write separate file for Row Type 300 only
with open(row300_output_path, "w", newline='') as row300_file:
    writer = csv.writer(row300_file)
    writer.writerow(headers["300"])  # Write header
    writer.writerows(row300_data)
