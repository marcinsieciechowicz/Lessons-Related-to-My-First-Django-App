# hasattr(object, name)

class Me:
    name = 'szuszwol'
    age = 28

somebody = Me

print('Does he have any age?: ', hasattr(somebody, 'age'))
print('Does he have salary??: ', hasattr(somebody, 'salary'))
