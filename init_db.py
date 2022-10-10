import os
import psycopg2



conn = psycopg2.connect(database="", # the database in which I created in psql
                        host="localhost",
                        user="postgres",
                        password="",
                        port="5432")

# Open a cursor to perform database operations
cur = conn.cursor()



# Execute a command: this creates a new table

cur.execute('DROP TABLE IF EXISTS members;')
cur.execute('create table members (
                                    id INT,
                                    first_name VARCHAR(50),
                                    last_name VARCHAR(50),
                                    email VARCHAR(50),
                                    eth_address VARCHAR(50),
                                    active VARCHAR(50)
                                );
                                



# Insert data into the table

cur.execute('INSERT INTO members (first_name, last_name, email, eth_address, active'
            'VALUES (%s, %s, %s, %s, %s)',
            ('Orion',
             'Ford',
             'DesignisO@Protonmail.com',
             '0xB8921C382c8936644F12F09DF29bc26084Bd5c5d',
             'True'
            )

cur.execute('INSERT INTO members (first_name, last_name, email, eth_address, active'
            'VALUES (%s, %s, %s, %s, %s)',
            ('Micah',
             'Ford',
             'Munchie@Protonmail.com',
             '0xbbe92e1f68e0a7834442fc4b7a0a07c622f783058ca0f5a185980031ffbc3eb7',
             'True'
            )
            
cur.execute('INSERT INTO members (first_name, last_name, email, eth_address, active'
            'VALUES (%s, %s, %s, %s, %s)',
            ('Johnny',
             'Thomas',
             'JTbot1@Protonmail.com',
             '0x8a2b3e7cc55e27c65f14f6fb56938f0d95d7908709b2fdf604ae395b50f845af',
             'False'
            )
            
conn.commit()

cur.close()
conn.close()