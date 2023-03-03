n = int(input('Your number is: '))
s = 0
i = 0
while s<=n:
    i += 1
    s += 1/i
if 5 <= i <= 20 or i % 10 == 0 or 5 <= i % 10 <= 9:
    right_word = 'parts'
elif i % 10 == 1:
    right_word = 'part'
else:
    right_word = 'part'
print(('You need to add {} {} sequence').format(i, right_word))