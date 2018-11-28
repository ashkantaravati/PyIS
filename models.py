from data_manager import Entity
class Person(Entity):
    entity_verbose_name = 'Person'
    def __init__(self, fname, lname):
        self.first_name = fname
        self.last_name = lname
    
    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    def __repr__(self):
        return f'{self.first_name} {self.last_name}'
    
class Car(Entity):
    entity_verbose_name='Car'
    def __init__(self, name, type):
        self.name = name
        self.type = type
    def __str__(self):
        return f'{self.name}'
    def __repr__(self):
        return f'{self.name}'