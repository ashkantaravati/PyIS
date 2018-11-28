from models import Person, Car
# import data_manager
def add_some_stuff_logic():

    # data = data_manager.load_data(Person)

    # print (data)


    p1 = Person('james','jackson')
    p2 = Person('Joan','Simpson')

    Person.add(p1)
    Person.add(p2)
    Person.save()

    c1 = Car('Ferrari','Sedan')
    c2 = Car('Peugeot', 'Station')

    Car.add(c1)
    Car.add(c2)
    Car.save()
    print(Car.show())