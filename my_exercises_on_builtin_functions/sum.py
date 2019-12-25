import math

numlist = ['12', '13', '14', '15']
separator = ', '
print(separator.join(numlist))

numtuple = ('12', '13', '14', '15')
print(separator.join(numtuple))

s1 = 'abc'
s2 = '123'

print('s1.join(s2):', s1.join(s2))
print('s2.join(s1):', s2.join(s1))

test = {'20', '1', '3'}
s = ', '

print(s.join(test))

test = {'Python', 'Java', 'Ruby'}
s = '->->'
print(s.join(test))

t_test = {'mat':1, 'that':2}
sep = '->'
print(sep.join(t_test))


suma = [2.5, 3.4, 3.09]
print(math.fsum(suma))

