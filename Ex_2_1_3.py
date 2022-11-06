num = int(input('Input number:'))
d_1 = 4
d_2 = 100
d_3 = 400
print('YES') if num % d_3 == 0 else print('NO') if num % d_2 == 0 else print('YES') if num % d_1 == 0 else print ('NO')