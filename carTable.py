import sqlite3

conn = sqlite3.connect('car.db')


with conn:
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS tbl_cars( \
        ID INTEGER PRIMARY KEY AUTOINCREMENT, \
        col_carName TEXT, \
        col_carYear TEXT, \
        col_carMaker TEXT \
        )")
    conn.commit()
conn.close()


conn = sqlite3.connect('car.db')

with conn:
    cur = conn.cursor()
    cur.execute("INSERT INTO tbl_cars(col_carName, col_carYear, col_carMaker) VALUES (?,?,?)", \
                ('Cruze', '2020', 'Chevy'))
    cur.execute("INSERT INTO tbl_cars(col_carName, col_carYear, col_carMaker) VALUES (?,?,?)", \
                ('Tacoma', '2023', 'Toyota'))
    cur.execute("INSERT INTO tbl_cars(col_carName, col_carYear, col_carMaker) VALUES (?,?,?)", \
                ('Altima', '2016', 'Nissan'))
    conn.commit()
conn.close()


conn = sqlite3.connect('car.db')


with conn:
    cur = conn.cursor()
    cur.execute("SELECT col_carName, col_carYear, col_carMaker FROM tbl_cars WHERE col_carName = 'Cruze'")
    varCars = cur.fetchall()
    for item in varCars:
        msg = "Car Name: {}\nCar Year: {}\nCar Maker: {}".format(item[0],item[1],item[2])
    print(msg)



