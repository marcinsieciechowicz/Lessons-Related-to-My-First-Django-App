# func that creates a set

nowy_set = set([1,2,3,4,2,3])
print(nowy_set)

# now creating a empty set

a = {}

print(type(a))

a = set()

print(type(a))


# adding new values to set

moj_set = {1,3}
moj_set.add(2)
print(moj_set)

moj_set.update([5,6,7])
print(moj_set)

moj_set.discard(6)
print(moj_set)