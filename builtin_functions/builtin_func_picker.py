import sqlite3

conn = sqlite3.connect('db')
with conn:
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()
    sql = 'SELECT name FROM builtin_funcs WHERE learned_on IS NULL ORDER BY RANDOM() LIMIT 1 '
    cur.execute(sql)
    row = cur.fetchone()
    random_builtin_func = row['name']
    url = 'https://docs.python.org/3/library/functions.html#' + random_builtin_func.replace('()', '')
    print(url)
    sql = 'UPDATE builtin_funcs SET learned_on = DATE() WHERE name = ?'
    cur.execute(sql, [random_builtin_func])

