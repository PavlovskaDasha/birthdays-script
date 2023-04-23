import collections
from datetime import datetime, timedelta, date, time

users = {'Nick': datetime(year=1962, month=4, day=28),
         'Jane': datetime(year=2004, month=4, day=29),
         'Anton': datetime(year=1987, month=4, day=25),
         'John': datetime(year=2020, month=9, day=23),
         'Kate': datetime(year=1995, month=3, day=23),
         'Oleg': datetime(year=1989, month=4, day=24),
         'Helen': datetime(year=2004, month=4, day=26),
         'Mike': datetime(year=2001, month=1, day=1),
         'Olga': datetime(year=1999, month=4, day=23)}


def get_birthdays_per_week(users, today=datetime.today()):
    today = datetime.combine(today, time.min)
    bdays = collections.defaultdict(list)
    next_monday = today + timedelta(days=7 - today.weekday())
    next_saturday = next_monday + timedelta(days=-2)
    for name, birth in users.items():
        birthday = birth.replace(year=today.year)
        if birthday < next_saturday:
            birthday = birth.replace(year=today.year + 1)
        if birthday - next_saturday >= timedelta(days=7):
            continue
        if birthday.weekday() > 4:
            bdays[next_monday].append(name)
        else:
            bdays[birthday].append(name)

    res = []
    for birthday in sorted(bdays.keys()):
        day = birthday.strftime("%A")
        res.append(day + ": " + ", ".join(bdays[birthday]))
    return "\n".join(res)


print(get_birthdays_per_week(users))
