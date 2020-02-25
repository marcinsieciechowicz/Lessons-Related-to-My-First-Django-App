print('int 123 is: ', int(123))


# example with class:

class Person:
    age = 28

    def __index__(self):
        return self.age

    def __int__(self):
        return self.age


person = Person()

print('int person is: ', int(person))