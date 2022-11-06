number = int(input('Input number:'))
divider_1 = 4
divider_2 = 100
divider_3 = 400
print('YES' if number % divider_3 == 0 else
      'NO' if number % divider_2 == 0 else
            'YES' if number % divider_1 == 0 else 'NO')