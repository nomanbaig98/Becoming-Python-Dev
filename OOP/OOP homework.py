# problem 1

class Line:
    def __init__(self, cord1, cord2):
        self.cord1 = cord1
        self.cord2 = cord2

    def distance(self):
        return (((self.cord1[0] - self.cord2[0]) ** 2) + ((self.cord1[1] - self.cord2[1]) ** 2)) ** 0.5

    def slope(self):
        return (self.cord2[1] - self.cord1[1]) / (self.cord2[0] - self.cord1[0])


coordinate1 = (3, 2)
coordinate2 = (8, 10)

li = Line(coordinate1, coordinate2)


# print(li.distance())

# print(li.slope())

# problem 2

class Cylinder:
    pi = 22 / 7

    def __init__(self, height=1, radius=1):
        self.height = height
        self.radius = radius


    def volume(self):
        return self.pi*self.radius*self.radius*self.height

    def surface_area(self):
        return ((2*self.pi*self.radius)*self.height)+((self.pi*self.radius**2)*2)


cyl =Cylinder(2,3)

print(cyl.volume())
print(cyl.surface_area())
print(cyl.pi)
print(cyl.height)
print(cyl.radius)