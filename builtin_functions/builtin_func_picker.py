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


# TODO:move the contents of the [builtin_functions] folder in the Lessons-Related-to-My-First-Django-App repo to a separate repository called Python Built-in Function of the Day Random Picker
# TODO:print the function of the day to learn only after the database was updated
# TODO:rename db to db.sqlite3
# TODO:run the script's main function only if the script is run in the main namespace (as opposed to being imported)
# TODO:the context manager does not close the connection automatically; it needs to be done manually
# TODO:use shortcut methods when appropriate (see: https://docs.python.org/3.7/library/sqlite3.html#using-shortcut-methods)
# TODO:Handle sqlite3 exceptions where appropriate (for the list of the available exceptions, see:  https://docs.python.org/3.7/library/sqlite3.html#exceptions)
# TODO:display Congratulations! You already know all Python built-in functions if there are no more functions to learn in the database
# TODO:remove () from built-in function names in the database (and get rid of the code that strips them in the script)
# TODO:add docstrings to function(s) (function description, param description (if any), return (if any), etc.)
# TODO:add type hints for function(s)
# TODO:how would you prevent the script from multiple random selections on a given day (e.g. in case the runner doesn't like the function that has been originally picked ;)); implement the anti-abuse strategy if you know how
# TODO:use the cursor as a context manager
# TODO:let the script handle the e-mail to Miko automatically
