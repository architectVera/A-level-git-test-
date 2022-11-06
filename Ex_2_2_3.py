fizz = int(input('Input fizz:'))
buzz =  int(input('Input buzz:'))
third = int(input('Input third:'))
i = 1
while i <= third:
      print('FB ' if not i % fizz and not i % buzz else 'F ' if not i % fizz else 'B ' if not i % buzz else i, end = ' ' )
      i = i + 1
