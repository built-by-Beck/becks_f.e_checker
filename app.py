from flask import Flask, render_template, request, redirect, url_for
import sqlite3
from datetime import datetime

app = Flask(__name__)

def get_db_connection():
    conn = sqlite3.connect('extinguisher.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/')
def index():
    sections = ['MOB_A', 'MOB_B', 'MOB_C', 'MOB_D', 'Employee_Parking_Deck', 'Visitor_Parking_Deck',
                'Womens_Medical_Center', 'Main_Hospital', 'FED']
    return render_template('index.html', sections=sections)

@app.route('/section/<section_name>')
def section_page(section_name):
    conn = get_db_connection()
    extinguishers = conn.execute('SELECT * FROM extinguishers WHERE section = ?', (section_name,)).fetchall()
    conn.close()
    return render_template('section.html', extinguishers=extinguishers, section_name=section_name)

@app.route('/mark_pass_fail/<int:id>', methods=['POST'])
def mark_pass_fail(id):
    status = request.form['status']
    conn = get_db_connection()
    conn.execute('UPDATE extinguishers SET pass_fail = ?, date_inspected = ? WHERE id = ?', 
                 (status, datetime.now().strftime("%Y-%m-%d"), id))
    conn.commit()
    conn.close()
    return redirect(url_for('section_page', section_name=request.form['section_name']))

if __name__ == '__main__':
    app.run(debug=True)
