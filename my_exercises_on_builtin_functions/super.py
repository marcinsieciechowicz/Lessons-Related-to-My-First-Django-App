# some example class and usage of super:


class Mammals(object):
    def __init__(self, name_of_mammal):
        print(name_of_mammal, 'moja Karmen jest piekna')


class Dog(Mammals):
    def __init__(self):
        print('Karmen jest sliczna')
        super().__init__('Dog')


d1 = Dog()


# Multiple inhetitance:

class Animal:
    def __init__(self, Animal):
        print(Animal, 'is a animal')


class Ssak(Animal):
    def __init__(self, name_of_mammal):
        print(name_of_mammal, 'cieplokrwisty')
        super().__init__(name_of_mammal)


class Bezskrzydlowiec(Ssak):
    def __init__(self):
        print(Bezskrzydlowiec, 'cannot fly')
        super().__init__(Bezskrzydlowiec)


d = Ssak('name_of_mammal')
print('')
karmen = Bezskrzydlowiec()
