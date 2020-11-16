from tests import *
import threading



def search_thread(start, stop, activity, county, list, file):
    timed_request(start, stop, activity, county, list, file)

data = []
file = "database.db"

x = datetime(2020, 11, 23)
y = datetime(2021, 1, 15)

searcher = threading.Thread(target=search_thread, args=(x, y, '1', '27', data, file))
searcher.start()
