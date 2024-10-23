import csv
import sqlite3

# Function to load CSV data into the database
def load_csv_to_db(csv_file_path, section_name):
    conn = sqlite3.connect('extinguisher.db')
    cursor = conn.cursor()

    with open(csv_file_path, 'r') as csv_file:
        reader = csv.DictReader(csv_file)

        for row in reader:
            cursor.execute('''
                INSERT INTO extinguishers (location_number, type, size, location, barcode, serial_number, pass_fail, date_inspected, initials, section)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            ''', (
                row['Location Number'], row['Type'], row['Size'], row['Location'],
                row['Barcode'], row['Serial Number'], 'Unchecked', '', '', section_name
            ))

    conn.commit()
    conn.close()

if __name__ == '__main__':
    # Load each section from the `csv` folder
    sections = ['csv/MOB_A.csv', 'csv/MOB_B.csv', 'csv/MOB_C.csv', 'csv/MOB_D.csv']  # Add other sections here

    for section_csv in sections:
        section_name = section_csv.split('/')[-1].split('.')[0]  # Extract section name from file name
        load_csv_to_db(section_csv, section_name)
