class Classy(object):
    def __init__(self):
        self.items = []
        items = self.items
        def adding_str(self):
            r = input('Give me a string')
            items.append(r)

# Test cases
me = Classy()

# Should be 0
print me.getClassiness()

me.addItem("tophat")
# Should be 2
print me.getClassiness()

me.addItem("bowtie")
me.addItem("jacket")
me.addItem("monocle")
# Should be 11
print me.getClassiness()

me.addItem("bowtie")
# Should be 15
print me.getClassiness()