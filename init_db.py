import sqlite3

def init_db():
    conn = sqlite3.connect('extinguisher.db')
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS extinguishers (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            section TEXT NOT NULL,
            location_number TEXT NOT NULL,
            type TEXT NOT NULL,
            size TEXT NOT NULL,
            location TEXT NOT NULL,
            barcode TEXT UNIQUE NOT NULL,
            serial_number TEXT NOT NULL,
            pass_fail TEXT DEFAULT 'Unchecked',
            date_inspected TEXT NOT NULL,
            initials TEXT NOT NULL
        );
    ''')

    conn.commit()
    conn.close()

if __name__ == '__main__':
    init_db()
