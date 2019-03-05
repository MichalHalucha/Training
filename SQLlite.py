import sqlite3

data = sqlite3.connect('my.db')
c = data.cursor()

c.execute("""CREATE TABLE stocks
             (date text, trans text, symbol text, qty real, price real)""")

c.execute("INSERT INTO stocks VALUES ('2006-01-05','BUY','RHAT',100,35.14)")



data.commit()

for row in c.execute('SELECT * FROM stocks ORDER BY price'):
    print(row)
data.close()


"""https://docs.python.org/2/library/sqlite3.html"""
