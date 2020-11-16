import pycurl
import json
import time
from datetime import datetime, timedelta
from utils import *
from io import BytesIO, StringIO


# --cURL requests to the site--
def request(start_date, stop_date, activity, county, list):
    c = pycurl.Curl()
    list.clear()
    while (start_date != stop_date):
        current = convert_to_string(start_date)
        url = 'https://www.drpciv.ro/drpciv-booking-api/getCalendar?start=' + current + '&end=' + current + '&activityCode=' + activity + '&countyCode=' + county
        c.setopt(c.URL, url)
        buf = BytesIO()
        c.setopt(c.WRITEDATA, buf)

        c.perform()

        body = buf.getvalue()
        ld = json.loads(body.decode('iso-8859-1'))
        for key in ld.keys():
             list.append(key)


        start_date = next_day(start_date)
    c.close()



def timed_request(start_date, stop_date, activity, county, data, file):
    starttime = time.time()
    while True:
        request(start_date, stop_date, activity, county, data)
        update_db(file, data)
        time.sleep(30.0 - time.time() % 30.0)
