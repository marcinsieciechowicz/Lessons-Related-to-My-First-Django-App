# the old method of making the method static, better is using decorators

class Matematyka:

    def add_num(x,y):
        return x+y

Matematyka.add_num = staticmethod(Matematyka.add_num)

print('suma wynosi: ', Matematyka.add_num(1,2))
