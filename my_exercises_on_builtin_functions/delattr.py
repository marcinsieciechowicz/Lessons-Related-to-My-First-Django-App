# delattr(object, name)

class szuszwol:
    a = 1
    b = 2
    c = 3

punkt_1 = szuszwol

print('a= ', szuszwol.a)
print('b= ', szuszwol.b)
print('c= ', szuszwol.c)

delattr(szuszwol, 'c')

print('a= ', szuszwol.a)
print('b= ', szuszwol.b)
print('after deleting c')

# try

print(szuszwol.c)
# error