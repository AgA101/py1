class Person:
    count_a = 2
    def green(self):
        print(f'Hi {self.name}!')
    def __init__(self,name):
        self.name = name

    def __str__(self):
        return f'Person<name={self.name}>'

    def __eq__(self, other):
        return self.name == other.name
me = Person('ni')
you = Person('li')
Person.count_a = 5
print(me,you)
clone = Person('ni')
print(me == clone)
me.green()
you.green()
