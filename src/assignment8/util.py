import datetime
def dayofweek(date):
    year, month, day = map(int, date.split('-'))
    a = datetime.date(year, month, day)
    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    return days[a.weekday()]