import random
print('task 1')
words = []
for i in range(1, 11):
    print('input {} word'.format(i))
    words.append(input())
for word in words:
    print(word, end= ', ')
print()

print('task 2')
numbers = []
for i in range(1, 11):
    print('input {} number'.format(i))
    numbers.append(int(input()))
for number in numbers:
    print(number, end= ', ')
print()

print('tsak 3')
rand_numbers = []
for i in range(1, 11):
    rand_numbers.append(random.randint(-30, 30))
for number in rand_numbers:
    print(number, end= ', ')
print()

print('tsak 4')
print(' Output in reverse order')
numbers.reverse()
for number in rand_numbers:
    print(number, end= ', ')
print()
print(' Output in ascending order')
rand_numbers.sort()
for number in rand_numbers:
    print(number, end= ', ')
print()
print('c) Output in descending order')
rand_numbers.sort(reverse= True)
for number in rand_numbers:
    print(number, end= ', ')
print()

print('task 5')
n = int(input('type n '))
m = int(input('type m '))
for number in rand_numbers[n:m+1]:
    print(number, end= ', ')
print()

print('task 6')
for number in rand_numbers:
    if number > 0:
        print(number)
print()

print('task 7')
for number in rand_numbers[ : : 2]:
    print(number)
print()

print('task 8')
for number in rand_numbers:
    if number % 2 == 0:
        print(number)
print()

print('task 9')
n = int(input('input number: '))
print(rand_numbers.index(n)+1 if rand_numbers.count(n) > 0 else 'Theres no number like this')
print()

print('task 10')
rand_numbers2 = []
for i in range(20):
    rand_numbers2.append(random.randint(-3,3))
for number in rand_numbers2:
    print(number, end=', ')
print()
i = 0
while(i < len(rand_numbers2)):
    if rand_numbers2[i] == 0:
        del rand_numbers2[i]
        continue
    i += 1
for number in rand_numbers2:
    print(number, end=', ')

print('task 11')
rand_numbers3 = []
for i in range(20):
    rand_numbers3.append(random.randint(-3,3))
for number in rand_numbers3:
    print(number, end=', ')
print()
i = 0
while(i < len(rand_numbers3)):
    if rand_numbers3[i] < 0:
        del rand_numbers3[i]
        continue
    i += 1
for number in rand_numbers3:
    print(number, end=', ')
