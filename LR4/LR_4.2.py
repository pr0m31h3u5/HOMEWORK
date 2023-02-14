pswd = False
while not pswd:
    print('Введите ваш пароль: ')
    input_pswd = input()
    if len(input_pswd) < 2:
        print("Пароль слишком короткий")
    else:
        print("Подтвердите ваш пароль: ")
        repeat_pswd = input()
        if repeat_pswd == input_pswd:
            print("Пароль подтверждён!")
            pswd = True
        else:
            print("Пароли различаются,попробуйте снова...")