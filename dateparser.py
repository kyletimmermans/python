import datetime
import re

'''
Convert time formats into timestamp then
into ISO-8601 format as datetime object

Working Formats (All return: 2021-07-20 16:44:39+00:00)

1626813879
"2021-07-20 16:44:39"
"2021-07-20T16:44:39Z"
"2021-07-20T16:44:39+00:00"
"2021-07-20 20:44:39 -0400"
"2021-07-20 16:44:39 +0000"
"2021-07-20T16:44:39.886515"
"2021-07-20T20:44:39.090-0400"
"Tue, 20 Jul 2021 20:44:39 -0400"
"Tue Jul 20 16:44:39 UTC 2021"
"16:44:39123+00:00 2021-07-20"
"2021/07/20 16:44:39"
"16:44:39 2021-07-20"
"2021-07-20 12:44:39 +0400"
"2021-07-20 04:44:39 +12:00"
'''


def iso_format(timestamp):  # Timestamp -> ISO-8601 Format
    temp = datetime.datetime.fromtimestamp(int(timestamp))
    return temp.replace(tzinfo=datetime.timezone.utc)


def timezone_logic(datestring):  # If timezone, set to UTC
    match1 = re.search("[-+]\d\d[0][0]", datestring)
    match2 = re.search("[-+]\d\d[:][0][0]", datestring)
    if match1:
        return int(match1.group().replace("0", ""))
    elif match2:
        return int(match2.group().replace("0", "").replace(":", ""))
    else:
        return 0


def parse_date(date):  # Remove extra chars, clean up, and parse date
    date = str(date).replace("UTC", "").replace("GMT", "")
    if re.search("[T]+\d", date):
        date = date.replace("T", "")
    date = date.replace("Z", "").replace("/", "-").replace(" ", "")
    date = date.replace("+0000", "").replace("+00:00", "")
    timezone_hours = timezone_logic(date)
    if date.isdigit():  # Timestamp format
        return iso_format(date)
    elif re.search("(Mon|Tue|Wed|Thu|Fri|Sat|Sun)", date):  # Day/month written
        date = date[3:].replace(",", "").replace(" ", "")
        if date[:2].isdigit():  # Day, month
            date = datetime.datetime.strptime(date[:17], "%d%b%Y%H:%M:%S")
            date = date + datetime.timedelta(hours=timezone_hours)
            return iso_format(date.timestamp())
        else:  # Month, day
            date = datetime.datetime.strptime(date[:20], "%b%d%H:%M:%S%Y")
            date = date + datetime.timedelta(hours=timezone_hours)
            return iso_format(date.timestamp())
    elif date[2] == ':':  # Time before date format
        date = f'{date[0:8]}{date[-10:]}'
        date = datetime.datetime.strptime(date, "%H:%M:%S%Y-%m-%d")
        date = date + datetime.timedelta(hours=timezone_hours)
        return iso_format(date.timestamp())
    elif len(date) <= 19:   # Dates before time format
        date = datetime.datetime.strptime(date, "%Y-%m-%d%H:%M:%S")
        date = date + datetime.timedelta(hours=timezone_hours)
        return iso_format(date.timestamp())
    else:
        date = datetime.datetime.strptime(date[:18], "%Y-%m-%d%H:%M:%S")
        date = date + datetime.timedelta(hours=timezone_hours)
        return iso_format(date.timestamp())
