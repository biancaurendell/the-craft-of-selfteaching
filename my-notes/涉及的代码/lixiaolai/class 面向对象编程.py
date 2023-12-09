import datetime

class Golem:

    def __init__(self, name=None):
        self.name = name
        self.built_year = datetime.date.today().year

    def say_hi(self):
        print('Hi!')

g = Golem('Clay')
print(g)
print(g.name)
print(g.built_year)
print(g.say_hi)
print(g.say_hi())
print(type(g))
print(type(g.name))
print(type(g.built_year))
print(type(g.__init__))
print(type(g.say_hi))