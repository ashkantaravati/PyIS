import random
from ..entities import student

def random_name():
    range_end = len(NAME_BANK) -1
    name1 = NAME_BANK[random.randint(0, range_end)]
    name2 = NAME_BANK[random.randint(0, range_end)]
    return f'{name1}{name2}'

def random_number():
    number = random.randint(9200000000, 9999999999)
    return str(number)

def random_mark():
    mark_int = random.randint(0, 2000)
    if mark_int == 0:
        return 0.0
    mark_float = float(mark_int)
    mark = mark_float / 100
    return mark


def random_student():
    name = random_name()
    number = random_number()
    mark = random_mark()
    new_student = student.Student(name,number,mark)
    return new_student

def random_student_list(num):
    slist = []
    for i in range(0,num):
        slist.append(random_student())
    return slist


NAME_BANK = [
    'ali',
    'amir',
    'hassan',
    'akbar',
    'naser',
    'karam',
    'kazem',
    'mohammad',
    ]
