num1 = int(input("Введите первое число: "))
num2 = int(input("Введите второе число: "))
if num1%num2 == 0:
    print("%d делится на %d" % (num1,num2))
else:
    print("%d не делится на %d" % (num1,num2))
    print("Остаток: %d" % (num1%num2))