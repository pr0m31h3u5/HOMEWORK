import math
people = float(input("Введите колличество людей: "))
bus = float(input("Введите вместимость автобусов: "))
bus_needed = people / bus
print("Вам понадобится ", math.ceil(bus_needed), "автобусов")