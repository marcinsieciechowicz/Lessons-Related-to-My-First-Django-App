# import sqlite3
#
# conn = sqlite3.connect('db')
# with conn:
#     conn.row_factory = sqlite3.Row
#     cur = conn.cursor()
#     sql = 'SELECT name FROM builtin_funcs WHERE learned_on IS NULL ORDER BY RANDOM() LIMIT 1 '
#     cur.execute(sql)
#     row = cur.fetchone()
#     random_builtin_func = row['name']
#     url = 'https://docs.python.org/3/library/functions.html#' + random_builtin_func.replace('()', '')
#     print(url)
#     sql = 'UPDATE builtin_funcs SET learned_on = DATE() WHERE name = ?'
#     cur.execute(sql, [random_builtin_func])

numlist = ['12', '13', '14', '15']
separator = ', '
print(separator.join(numlist))

numtuple = ('12', '13', '14', '15')
print(separator.join(numtuple))

s1 = 'abc'
s2 = '123'

print('s1.join(s2):', s1.join(s2))
print('s2.join(s1):', s2.join(s1))