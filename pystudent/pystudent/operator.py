''' dostring  '''
def save_as_txt(classroom):
    ''' docstring  '''
    print('saved to txt file')

def print_to_screen(classroom):
    ''' prints data '''
    for student in classroom.students:
        print(f'{student.name} {student.number} {student.mark}')
    print(f'Class average is {classroom.subject_average()}')

def save_as_json(classroom):
    ''' json '''
    print('saved to json file')