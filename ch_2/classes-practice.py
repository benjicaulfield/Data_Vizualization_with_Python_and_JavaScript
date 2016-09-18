__author__ = 'Bradley'

class Citizen(object):

    def __init__(self, name, country):
        self.name = name
        self.country = country

    def print_details(self):
        print("Citizen %s from %s" %(self.name, self.country))

c = Citizen('Groucho M.', 'Freedonia')
c.print_details()

class Winner(Citizen):

    def __init__(self, name, country, category, year):
        super(Winner, self).__init__(name, country)
        self.category = category
        self.year = year

    def print_details(self):
        print("Nobel winner %s from %s, category %s, year %s" \
              %(self.name, self.country, self.category, \
                str(self.year)))

w = Winner('Albert E.', 'Switzerland', 'Physics', 1921)
w.print_details()

def fibonacci(n):
    x, y = 0, 1
    for i in range(n):
        print(x)
        x, y = y, x + y

fibonacci(10)