import random as r
from time import sleep
import names
import os
from tqdm import tqdm
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


number = 250

try:
    while number:
        for i in tqdm(range(number)):
            with open(FILE_PATH, 'a+') as file_txt:
                one_line = [name(), city(), phone()]
                result_str = one_line[0].ljust(22) + one_line[1].ljust(22) + one_line[2].ljust(15) + dtime()
                file_txt.write(result_str + '\n')
                file_txt.close()
                number -= 1
                sleep(0.01)
except EOFError:
    print('Hello, user it is EOF exception, please enter something and run me again')
except KeyboardInterrupt:
    print('Hello, You have just stopped the process.')
else:
    print('Hello, everything is done')