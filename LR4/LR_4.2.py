pswd = False
while not pswd:
    print('Введите ваш пароль, используя только числа: ')
    input_pswd = int(input())
    repeat_pswd = int(input())
    if repeat_pswd == input_pswd:
        print("Пароль подтверждён!")
        pswd = True
    else:
        print("Пароли различаются,попробуйте снова...")