class Classy(object):
    def __init__(self):
        self.items = []

    def addItem(self, items):
        self.items.append(items)

    def getClassiness(self):
        classiness = 0
        for element in self.items:
            if element == 'tophat':
                classiness += 2
            elif element == 'bowtie':
                classiness += 4
            elif element == 'monocle':
                classiness += 5
            else:
                classiness += 0
        return classiness

# Test cases
me = Classy()

# Should be 0
print(me.getClassiness())

me.addItem("tophat")
# Should be 2
print(me.getClassiness())

me.addItem("bowtie")
me.addItem("jacket")
me.addItem("monocle")
# Should be 11
print(me.getClassiness())

me.addItem("bowtie")
# Should be 15
print(me.getClassiness())