import math
n = float(input('Введите градусы угла синуса: '))
n_rad = n*math.pi/180 
sinus = math.sin(n_rad) 
print('Радиан в синусе: ', n_rad)
print('sin равен: ', sinus)