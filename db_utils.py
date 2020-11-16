import sqlite3
import time


def clear_db(filename):
    connection = sqlite3.connect(filename)
    cursor = connection.cursor()

    #Delete previous data
    cursor.execute("TRUNCATE TABLE available")


def update_db(filename, list):
    connection = sqlite3.connect(filename)
    cursor = connection.cursor()

    for date in list:
        cursor.execute("INSERT INTO available VALUES(?)", date)

    connection.commit()
    connection.close()




def read_db(filename, list):
    #TODO
