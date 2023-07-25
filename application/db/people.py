__employee_names__ = [
    'Alex',
    'Michail',
    'Tom',
    'Alexandr'
]


def get_employees(emp_id):
    return __employee_names__[emp_id % len(__employee_names__)]
