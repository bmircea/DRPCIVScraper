import sqlite3
from datetime import datetime, timedelta


#   --DB utils--
def update_db(filename, list):
    connection = sqlite3.connect(filename)
    cursor = connection.cursor()

    # --Delete previous data--
    cursor.execute("DELETE FROM available")
    # ----

    for date in list:
        cursor.execute("INSERT INTO available VALUES(?)", (date,))

    connection.commit()
    connection.close()

#   --DateTime utils--
def next_day(date):
    tomorrow = timedelta(days=+1)
    return date+tomorrow

def convert_to_string(date):
    y = date.strftime("%Y")
    m = date.strftime("%m")
    d = date.strftime("%d")
    if (m[0] == '0'): m = m[1:]
    if (d[0] == '0'): d = d[1:]
    return y + '-'+ m + '-' + d

def convert_to_date(date):
    print(date)
    return datetime.strptime(date, "%Y/%m/%d %H:%M")
