# import math
 
# print("Введите коэффициенты для уравнения")
# print("ax^2 + bx + c = 0:")
# a = float(input("a = "))
# b = float(input("b = "))
# c = float(input("c = "))
 
# discr = b ** 2 - 4 * a * c
# print("Дискриминант D = %.2f" % discr)
 
# if discr > 0:
#     x1 = (-b + math.sqrt(discr)) / (2 * a)
#     x2 = (-b - math.sqrt(discr)) / (2 * a)
#     print("x1 = %.2f \nx2 = %.2f" % (x1, x2))
# elif discr == 0:
#     x = -b / (2 * a)
#     print("x = %.2f" % x)
# else:
#     print("Корней нет")

# print('Решаем уравнение a•x²+b•x+c=0')
# a = input('Введите значение a: ')
# b = input('Введите значение b: ')
# c = input('Введите значение c: ')
# a = float(a)
# b = float(b)
# c = float(c)
# discriminant = b**2 - 4*a*c
# print('Дискриминант = ' + str(discriminant))
# if discriminant < 0:
#     print('Корней нет')
# elif discriminant == 0:
#     x = -b / (2 * a)
#     print('x = ' + str(x))
# else:
#     x1 = (-b + discriminant ** 0.5) / (2 * a)
#     x2 = (-b - discriminant ** 0.5) / (2 * a)
#     print('x₁ = ' + str(x1))
#     print('x₂ = ' + str(x2))


from math import sqrt
a = float(input("a = "))
b = float(input("b = "))
c = float(input("c = "))
if a != 0:
    if  b !=0:
        d = b*b - 4*a*c
        print("D=", d)
        if d < 0:
            print("Нет корней")
        else:
            x1 = (-b + sqrt(d)) / (2*a)
            x2 = (-b - sqrt(d)) / (2*a)
            if x1 < x2:
                print("x2-это больший корень",x2)
            elif x1 > x2:
                print("x1-это больший корень",x1)
else:
    print("a = 0 - это не квадратное уравнение")




# num1 = int (input ("Введите певрое число: "))
# num2 = int (input ("Введите второе число: "))
# if num1 < num2:
#     print(num2)
# elif num1 > num2:
#     print(num1)