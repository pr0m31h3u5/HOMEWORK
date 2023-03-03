n = int(input(' n =  '))
for i in range(n):
    new = int(input('number =  '))
    if i == 0:
        max = new
    else: max = new if new > max else max
print('max num = ', max)
