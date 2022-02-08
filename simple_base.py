import random as r
import names
import os
from datetime import datetime, timedelta
from pathlib import Path

FILE_PATH = os.path.join(os.path.expanduser('~'), 'Desktop',
                         'clients.txt')  # link to user's desktop
path = Path(FILE_PATH)


def dtime():
    min_year = 1980
    max_year = datetime.now().year - 1
    start = datetime(min_year, 1, 1, 00, 00, 00)
    years = max_year - min_year + 1
    end = start + timedelta(days=365 * years)
    random_date = start + (end - start) * r.random()
    new_random_date = str(random_date).split(".")
    return new_random_date[0]


def phone():
    first = str(r.randint(100, 999))
    second = str(r.randint(1, 888)).zfill(3)
    last = (str(r.randint(1, 9998)).zfill(4))
    while last in ['1111', '2222', '3333', '4444', '5555', '6666', '7777', '8888']:
        last = (str(r.randint(1, 9998)).zfill(4))
    return f'{first}-{second}-{last}'


def city():
    city = r.choice(open('USA_Cities.txt').readlines())[:-1]
    return city


def name():
    name = names.get_full_name()
    return name


number = 200

start_time = datetime.now()

try:
    while number:
        with open(FILE_PATH, 'a+') as file_txt:
            result_str = name().ljust(22) + city().ljust(22) + phone().ljust(15) + dtime()
            file_txt.write(result_str + '\n')
        # print(number)   # to view the progress. Just to control the process
        number -= 1
except KeyboardInterrupt:
    print('Hello, You have just stopped the process.')

print(datetime.now() - start_time, 'отсчет закончен')