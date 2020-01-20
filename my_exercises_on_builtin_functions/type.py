# type: # can have one one argument or three arguments or type(name, bases, dict)

list = [1, 2, 3]

print(type(list))


class Foo:
    a = 0

foo = Foo()

print(type(foo))

# type() obtain three arguments:

obj_1 = type('X', (object,), dict(a='Foo', b='12'))
print(type(obj_1))
print(vars(obj_1))

