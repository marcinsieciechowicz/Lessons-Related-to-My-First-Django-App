from math import *
# syntax: exec(object, globals(optional), locals(optional)

program = 'a = 5\nb=10\nprint("Suma =", a+b)'
exec(program)


exec('print(dir())', {})
