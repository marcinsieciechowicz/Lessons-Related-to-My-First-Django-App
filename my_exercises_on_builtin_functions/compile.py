# syntax: compile(source, filename, mode, flags=0, dont_inherit=False, optimize=-1)

# example:

codeInString = 'a = 5\nb=6\nsum=a+b\nprint("sum =",sum)'
codeObejct = compile(codeInString, 'sumstring', 'exec')

exec(codeObejct)