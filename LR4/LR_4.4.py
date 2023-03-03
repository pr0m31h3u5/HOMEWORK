n = int(input(' n =  '))
sum1 = 0
for i in range(1, n+1):
    sum1 += i**2
print(('Sum of squares of numbers from 1 to {} = {}').format(n, sum1))
# второй вариант
n = int(input(' n =  '))
i = n
sum2 = 0
while i >= 1:
    sum2 += i**2
    i -= 1
print(('Sum of squares of numbers from 1 to {} = {}').format(n, sum2))