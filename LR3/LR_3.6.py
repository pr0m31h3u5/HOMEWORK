days = [ 'Понедельник', 'Вторник', 'Среда', 'Четверг', 'Пятница', 'Суббота', 'Воскресенье' ]
usr_day = 0 
while (usr_day < 1) or (usr_day > 7): 
    usr_day = int(input('Введите номер дня недели: '))    
    if(usr_day>7):
        print("В неделе семь дней, пробуй еще раз")
print(days[usr_day-1])