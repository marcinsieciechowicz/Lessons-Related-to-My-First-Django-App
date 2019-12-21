import abc
from abc import ABC, abstractclassmethod


class AbstractOperation(ABC):

    def __init__(self, operand_a, operand_b):
        self.operand_a = operand_a
        self.operand_b = operand_b
        super(AbstractOperation, self).__init__()

    @classmethod
    @abc.abstractmethod
    def do_something(self):
        pass


class ConcreteOperation(AbstractOperation):
    pass


class AddOperation(AbstractOperation):
    def execute(self):
        return

class Fam_member:
    def __init__(self, surname):
        self.l_name = surname

    def surname(self):
        print(self.l_name)


class Nicolas(Fam_member):
    def __init__(self, surname, f_name):
        super().__init__(surname)
        self.f_name = f_name

    def name(self):
        print(self.f_name)

    def full_name(self):
        print(self.f_name, self.l_name)


nico = Nicolas('Sieciechowicz', 'Mikolaj')
nico.surname()
nico.name()
nico.full_name()
fam_mem = Fam_member('Sieciechowicz')
fam_mem.surname()

# learn about BUILT-IN FUNCTIONS from python.docs, 1 per day (there are about 70), also pythoninstitute (1 hour/day) making a course,
# watch youtube films from user (added to favourites)
