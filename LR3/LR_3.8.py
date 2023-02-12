time = float(input("Сколько часов есть у агента: "))
speed = float(input("С какой скоростью он двигается (км/ч): "))
distance = float(input("Сколько километров он должен преодолеть (км): "))
answr = distance / time
if time > distance:
    print("агент успеет")
else:
    print("агент не успеет")