# syntax: bytes([source[, encoding(optional)[, errors(optional)]]]), similar to bytearrays

my_string = 'Szuszwol to Szuszwol'

argh = bytes(my_string, 'utf-8')
print(argh)

rozmiar = 234

rozmiar_2 = bytes(rozmiar)
print(rozmiar_2)