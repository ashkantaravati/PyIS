''' dostring  '''
from pystudent import entities
from pystudent import operator
from pystudent.mocklib import studentgen




class Manager:
    ''' CLI Manager '''
    managed_classrooms = []
    def register_classroom(self, classroom_obj):
        ''' docstring   '''
        self.managed_classrooms.append(classroom_obj)

    def register_classroom_student(self, student_obj, classroom_name):
        ''' docstring   '''
        #  self.managed_classrooms
        pass
    def show_resgistered(self):
        ''' docstring   '''
        return str(self.managed_classrooms)

def bulk_insert_student(classroom_obj):
    students = studentgen.random_student_list(8)
    for student in students:
        classroom_obj.add_student(student)

        
def main():
    ''' main function '''
    manager = Manager()
    my_class_room = entities.classroom.ClassRoom('room 1', entities.subject.SUBJECT_TYPES['Math'])
    manager.register_classroom(my_class_room)
    bulk_insert_student(my_class_room)

    operator.print_to_screen(my_class_room)
    operator.save_as_txt(my_class_room)

if __name__ == '__main__':
    main()
