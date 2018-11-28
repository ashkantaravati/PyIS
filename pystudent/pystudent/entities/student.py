'''   '''
class Student:
    ''' Student Entity '''
    def __init__(self, name, number, mark=0.0):
        self.name = str(name)
        self.number = str(number)
        self.mark = float(mark)