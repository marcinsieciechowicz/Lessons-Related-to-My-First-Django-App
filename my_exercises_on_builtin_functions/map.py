# syntax: map(function, iterable)

def calculate_sth(a):
    return a*a

nums = (1, 2, 3, 4)

wynik = map(calculate_sth, nums)
print(wynik)


numbersquare = set(wynik)
print(numbersquare)
