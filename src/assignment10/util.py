from datetime import datetime
def time_diff(t1, t2):
    format = "%a %d %b %Y %H:%M:%S %z" 

    date1 = datetime.strftime(t1, format)
    date2 = datetime.strftime(t2, format)

    return int(abs((date1-date2).total_seconds))