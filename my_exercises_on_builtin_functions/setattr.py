class Person:
    name = 'Adam'


p = Person()
print('Before modification:', p.name)

setattr(p, 'name', 'John')
print('After modification:', p.name)