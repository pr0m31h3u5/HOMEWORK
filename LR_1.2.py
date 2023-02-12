import math
class circle():
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        return math.pi * (self.radius**2)
    def perimeter(self):
        return 2 * math.pi * self.radius
 
r = int(input("Заданный радиус круга: "))
obj = circle(r)
print("Площадь равна:", round(obj.area(), 2))
print("Длина окружности равна:", round(obj.perimeter(), 2))