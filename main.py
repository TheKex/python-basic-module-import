from application.salary import calculate_salary
from application.db.people import get_employees
from datetime import datetime
import time
from faker import Faker


def print_current_time(func):
    def wrapper(*args, **kwargs):
        print(datetime.now())
        func(*args, **kwargs)
    return wrapper


@print_current_time
def main_func_1():
    print('Main func #1')


@print_current_time
def main_func_2(name, age):
    print(f'Main func #1 {name}, {age}')


if __name__ == '__main__':
    fake = Faker()
    print(calculate_salary(1, 10_000))
    print(get_employees(11))
    print(fake.name())
    main_func_1()
    time.sleep(4)
    main_func_2('Alex', age=12)


