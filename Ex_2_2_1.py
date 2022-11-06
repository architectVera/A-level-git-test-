fizz = int(input('Input fizz:'))
buzz =  int(input('Input buzz:'))
third = int(input('Input third:'))
i = 1
while i <= third:
      print('FB ' if i % fizz == 0 and i % buzz == 0 else 'F ' if i % fizz == 0 else 'B ' if i % buzz == 0 else i, end = ' ' )
      i = i + 1
