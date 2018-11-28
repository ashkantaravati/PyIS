'''   '''
class ClassRoom:
    ''' ClassRoom Entity '''
    def __init__(self, name, subject):
        self.name = str(name)
        self.students = list()
        self.subject = subject
    def add_student(self, student):
        ''' adds passed student object to list '''
        self.students.append(student)
    def subject_average(self):
        '''  Gets average of classroom marks '''
        sum_of_marks = float()
        number_of_students = len(self.students)
        for student in self.students:
            sum_of_marks += student.mark
        average = sum_of_marks / number_of_students
        return average