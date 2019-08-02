import sqlite3 as sql3
import dategen


#adds single day
def AddDay(day, cursor):
    cursor.execute("INSERT INTO date VALUES (?, ?)", (day.date, day.name))
#automatets addition of days togheter
def AddDays():
    days = int(input("Give us number of days:"))
    first_day = input("Give us first day:")
    test = dategen.Generator(days, first_day)
    for day in test:
        AddDay(day, c)

conn = sql3.connect("timebank.db")


c = conn.cursor()

#c.execute("""CREATE TABLE date (
#            date integer,
#            name text
#)""")
c.execute("SELECT * FROM date")
DAYS = c.fetchall()
print(DAYS[19])


conn.commit()
conn.close()
