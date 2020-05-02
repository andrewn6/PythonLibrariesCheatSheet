import sqlite3
import time
import datetime
import random
#import matplotlib.pyplot as plt
#import matplotlib.dates as mdates
#from matplotlib import style

# style.use('fivethirtyeight')

# Defining a connection to cheatsheet.db and creating a database at the same time
# Automatically creates the db file if you do not have it
conn = sqlite3.connect('cheatsheet.db')


# You can also use your memory as a temporary database
# conn = sqlite3.connect(':memory:')

# Define a cursor (cursor basically does all things like
# adding,inserting,deleting,updating data, etc.)
c = conn.cursor()

# A database contains a lot of tables and tables contains a lot of data


'''
Defining a function to create a table(named stuffsToPlot)

Then in the table stuffToPlot, we need to define our data variable name and their own data type

Table Data Types
INTEGER - Integer
REAL - Float
TEXT - String
NULL - Null/NaN
BLOB - A Blob of Value (Stored exactly as it was input)
#########################################
You will also notice that there are some uppercase and lowercase letters, it is just some kind of convention to follow

UPPERCASE - code that are for sql
lowercase - code that is not for sql
'''


def createTable():
    c.execute(
        'CREATE TABLE IF NOT EXISTS stuffToPlot(unix REAL, datestamp TEXT, keyword TEXT, value REAL)')


# Input data to the database by inserting data in the parenthesis as the
# same exact order you did in column at the createTable function
def data_entry():
    c.execute('INSERT INTO stuffToPlot VALUES(162738362, "2020-04-20", "Python", 5)')
    conn.commit()  # Saves what you did/modified


# Inserting variables to tables
def dynamic_data_entry():
    unixTime = time.time()
    date = str(datetime.datetime.fromtimestamp(
        unixTime).strftime('%Y-%m-%d %H:%M:%S'))
    keyword = "Python"
    value = random.randrange(1, 10)

    # After the 'INSERT INTO table', you need to specify specific order of your table/column
    # then in the 'VALUES(?,?,?,?)' question marks are just placeholders
    # Then, you need to add a comma, then make a tuple with the variables
    # inside it
    c.execute(
        'INSERT INTO stuffToPlot (unix, datestamp, keyword, value) VALUES(?,?,?,?)',
        (unixTime,
         date,
         keyword,
         value))

    conn.commit()  # Do not forgetti


def read_from_db():
    # Selecting all columns from stuffToPlot
    c.execute('SELECT * FROM stuffToPlot')

    # Using logic in selecting - WHERE
    #c.execute('SELECT * FROM stuffToPlot WHERE value=3')

    # Multiple Logics in Selecting
    #c.execute("SELECT * FROM stuffToPlot WHERE value=3 AND keyword='Python'")

    # Changing order of the columns
    #c.execute('SELECT keyword,value,unix,datestamp FROM stuffToPlot')

    # Getting some columns, and not all
    #c.execute('SELECT keyword,unix FROM stuffToPlot')

    # Getting all the data from stuffToPlot
    #data = c.fetchall()
    # print(data) #Doing this is not good. Its printing messy stuffs

    # Iterating through each row is better
    for row in c.fetchall():
        print(row)
        # print(row[0]) #Prints specific column

    # We do not have to use conn.commit() here because we do not modify this database
    # Instead we just get data from it


# Graphing our data using matplotlib
def graph_data():
    c.execute('SELECT unix, value FROM stuffToPlot')
    dates = []
    values = []
    for row in c.fetchall():
        dates.append(datetime.datetime.fromtimestamp(row[0]))
        values.append(row[1])

    plt.plot_date(dates, values, '-')
    plt.show()


# Deleting and Updating - when you update a column, there are no undo's
def del_and_update():
    c.execute('SELECT * FROM stuffToPlot')
    [print(row) for row in c.fetchall()]

    # This is where you update a column using logics, SET is where you put
    # your value
    c.execute('UPDATE stuffToPlot SET value = 99 WHERE value = 3')

    conn.commit()  # Do not forget, we modified something, we need to save it
    print("#" * 50)
    c.execute('SELECT * FROM stuffToPlot')
    [print(row) for row in c.fetchall()]

    # You can also use variables when updating
    # Make sure the SQL statement must have all the values in ? or else it
    # will not work
    someVal = 99
    c.execute('UPDATE stuffToPlot SET value = (?) WHERE value = (?)', (someVal, 3))

    # Deleting Columns or data
    c.execute('DELETE FROM stuffToPlot value=99')
    conn.commit()

    # If you want to delete something you need to see its value firsf, because
    # you do not want to delete item accidentally
    c.execute('SELECT * FROM stuffToPlot WHERE value=2')
    [print(row) for row in c.fetchall()]

    # You can not also print c.fetchall because once you called it, you need to run select statement again
    # Use length function to see how many items will be deleted
    c.execute('SELECT * FROM stuffToPlot WHERE value=2')
    print(len(c.fetchall()))


# createTable() #You can run this just once to save time
# data_entry()
'''
#Made a copy of each column to populate our database

for i in range(10):
	dynamic_data_entry()
	time.sleep(1)
'''

# read_from_db()

# graph_data()

# del_and_update()

c.close()  # Closes the cursor(to save memory)
conn.close()  # Closes the connection(to save memory)
