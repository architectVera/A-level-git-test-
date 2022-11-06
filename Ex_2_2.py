fizz = int(input('Input fizz:'))
buzz =  int(input('Input buzz:'))
third = int(input('Input third:'))
i = 1
while i <= third:
      if i % fizz == 0 and i % buzz == 0:
            print('FB', end = ' ')
      elif i % fizz == 0:
            print('F',end = ' ')
      elif i % buzz == 0:
            print('B',end = ' ')
      else:
            print(i,end = ' ')
      i = i + 1
