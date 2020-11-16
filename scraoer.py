import pycurl
import json
import time
from datetime import datetime, timedelta
from db_utils import *
from io import BytesIO, StringIO


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

def convert_to_date(date, time):
    string = date + " " + time
    return datetime.strptime(string, "%Y/%m/%d %H:%M")

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
        update_file(file, data)
        time.sleep(30.0 - time.time() % 30.0)
