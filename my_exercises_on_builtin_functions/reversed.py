# examples:

some_sequence = 'szuszwol'

print(list(reversed(some_sequence)))

marcin = 'geniusz'

print(tuple(reversed(marcin)))


class samogloski:
    vowels = ['a', 'o', 'e', 'i', 'u', 'y']

    def __reversed__(self):
        return reversed(self.vowels)


v = samogloski()
print(list(reversed(v)))
