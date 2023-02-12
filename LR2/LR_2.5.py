def convert(sec):
    sec = sec % (24 * 3600)
    hour = sec // 3600
    sec %= 3600
    min = sec // 60
    sec %= 60
    return "%02d:%02d:%02d" % (hour, min, sec)
time_min = float(input("введите интервал в секундах: "))
print("ЧЧ:ММ:СС -- ", convert(time_min))
