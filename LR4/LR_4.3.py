# for pswd in range(5):
#     pswd = False
#     while not pswd:
#         print('Введите ваш пароль, используя только числа: ')
#         input_pswd = int(input())
#         repeat_pswd = int(input())
#         if repeat_pswd == input_pswd:
#             print("Пароль подтверждён!")
#             pswd = True
#         else:
#             print("Пароли различаются,попробуйте снова...")

password = '123456'
input_password = input('Введите ваш пароль: ')
for i in range(4, 0, -1):
    if input_password != password:
        print(('Пароли различаются,попробуйте снова. У вас осталось {} попыток').format(i))
        input_password = input()
    if input_password == password:
        break
if input_password == password:
    print('Пароль Верный')
else:
    print('Попытки закончились')