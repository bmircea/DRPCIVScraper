import csv
import sys
import time

#TODO: have to switch to MySQL

def clear_file(filename):
    #Clear the file before writing the new data
    f = open(filename, "w")
    f.truncate()
    f.close()


def update_file(filename, list):
    data = open(filename, "w", newline='')
    # Set fieldnames (for date and time) and instantiate writer
    fieldnames = ['Date', 'Time']
    dialect = csv.excel
    dialect.delimiter = " "
    writer = csv.DictWriter(data, fieldnames=fieldnames, dialect=dialect)

    #Start writing header + data from dict
    writer.writeheader()
    for x in list:
        load = x.split(" ")
        writer.writerow({'Date': load[0], 'Time': load[1]})
    sys.stdout.write("Data written")
    print(time.time())
    data.close()




def read_file(filename, lista):
    #Assume that list is empty
    with open(filename, "r") as data:
        #TODO : Have to do this better. ATM using nested lists
        reader = csv.DictReader(data)
        for row in reader:
            x = list(row.items())[0][1].split(" ")
            lista[0].append(x[0])
            lista[1].append(x[1])

    data.close()
