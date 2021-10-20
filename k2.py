class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    #def __copy__(self):

    def distance(self,other):
        return ((self.x - other.x) ** 2 + (self.y - other.y) ** 2) ** 0.5

class Triangle:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
    def perimeter(self):
        return a.distance(b) + a.distance(c) + b.distance(c)
    #def area(self):
    #def __contains__(self,point):
a = Point(1,0)
z = a

b = Point(0,1)
c = Point(0,0)
tri = Triangle(a,b,c)
print(tri.perimeter())
#print(tri.c.x)