number = int(input('Input number:'))
divider_1 = 4
divider_2 = 100
divider_3 = 400
if number % divider_3 == 0:
    print('YES')
elif number % divider_2 == 0:
    print('NO')
elif number % divider_1 == 0:
    print('YES')
else:
    print('NO')
#print(number % 4 and 'NO' or 'YES')