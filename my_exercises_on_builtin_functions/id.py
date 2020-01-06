class Foo:
    a = 5

nextFoo = Foo
print('id of next Foo:', id(nextFoo))

print('id of a:', id(5))

b = 10

print('id of b:', id(b))

a = b

print('id of a:', id(a))

c = 15-5

print('id of c:', id(c))