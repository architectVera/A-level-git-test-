with open('file_1.txt', 'r') as fl:
    result = fl.read().split('\n')
    for line in result:
        numbers = line.split(' ')
        fizz = int(numbers[0])
        buzz = int(numbers[1])
        third = int(numbers[2])
        i = 1
        while i <= third:
             print('FB ' if not i % fizz and not i % buzz else 'F ' if not i % fizz else 'B ' if not i % buzz else i, end = ' ' )
             i = i + 1
        print('')





