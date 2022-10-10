import os
import psycopg2
from flask import Flask, render_template, request, url_for, redirect


app = Flask(__name__)

def get_db_connection():
    conn = psycopg2.connect(database="", # the database in which I created in psql
                        host="postgres",
                        password="",
                        port="5432")
    return conn

# created by Orion3000

@app.route('/')
def index():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('SELECT * FROM members;')
    members = cur.fetchall()
    cur.close()
    conn.close()
    return render_template('index.html', members=members)
    

@app.route('/create/', methods=('GET', 'POST'))
def create():
    if request.method == 'POST':
        student_id = request.form['student_id']
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        email = request.form['email']
        eth_address = request.form['eth_address']
        active = request.form['active']

        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute('INSERT INTO members (id, first_name, last_name, email, eth_address, active)'
                    'VALUES (%s, %s, %s, %s, %s, %s)',
                    (id, first_name, last_name, email, eth_address, active))
        conn.commit()
        cur.close()
        conn.close()
        return redirect(url_for('index'))

    return render_template('create.html')
    

if __name__ == "__main__":
    app.run(debug=True)
