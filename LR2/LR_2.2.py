lenght = float(input("введите длину помещения: "))
width = float(input("введите ширину помещения: "))
hight = float(input("введите высоту помещения: "))
s = lenght*width
wall_s = lenght*hight
vol = lenght*width*hight
print("площадь пола равна: ", s , "," , "площадь стен равна: ", wall_s, ",", "объём помещения равен: ", vol)