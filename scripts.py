import datetime
from datetime import timedelta


def add_days(date, add):
    date1 = datetime.datetime.strptime(str(date), "%d/%m/%Y").date()
    date = date1 + timedelta(days=add)
    return date


def check_for_notification(date, project_time):
    if date:
        if '-' in date:
            date = date.replace('-', '/')
            date = date.split('/')
            date.reverse()
            date = '/'.join(date)
            date = str(date)

        d1 = datetime.datetime.strptime(date, "%d/%m/%Y").date()
        d2 = datetime.datetime.now().date()

        t1 = datetime.datetime.strptime(project_time, '%H:%M').time()

        current_date_time = datetime.datetime.now()
        t2 = current_date_time.time()

        if (d2 >= d1 and t2 >= t1):
            return True
        else:
            return False

