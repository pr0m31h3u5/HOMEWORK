import random
def convert(min):
    min = min % (24 * 60)
    hour = min // 60
    min %= 60
    return "%02d:%02d:" % (hour, min, )
print("вывод случайных минут от 100 до 1000", convert(random.randint(100,1000)))




# import random
# def convert(sec):
#     sec = sec % (24 * 3600)
#     hour = sec // 3600
#     sec %= 3600
#     min = sec // 60
#     sec %= 60
#     return "%02d:%02d:%02d" % (hour, min, sec)
# print("вывод случайных секунд от 100 до 1000", convert(random.randint(100,1000)))

