import sqlite3
import csv

def load_csv_to_db(csv_file_path, section_name):
    conn = sqlite3.connect('extinguisher.db')
    cursor = conn.cursor()

    with open(csv_file_path, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            cursor.execute('''
                INSERT INTO extinguishers (section, location_number, type, size, location, barcode, serial_number, pass_fail, date_inspected, initials)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            ''', (section_name, row['Location Number'], row['Type'], row['Size'], row['Location'], 
                  row['Barcode'], row['Serial Number'], 'Unchecked', row['Date Inspected'], row['Initials']))
        conn.commit()
        conn.close()

if __name__ == '__main__':
    # Load each section
    sections = ['MOB_A.csv', 'MOB_B.csv', 'MOB_C.csv', 'MOB_D.csv']  # Add other sections here
    for section_csv in sections:
        section_name = section_csv.split('.')[0]
        load_csv_to_db(section_csv, section_name)
