list_1 = [1,2,3,4,5,6,7,8,10,9]

for i in range(len(list_1)):
    if i == 0:
        continue
    elif i % 2 == 0:
        print(list_1[i])
    else:
        continue
print('')
sum = 0
for i in list_1:
    sum += i
print(sum)
print('')
sum_even = 0
sum_odd = 0
for i in list_1:
    if i %2:
        sum_odd += i
    else:
        sum_even += i
print('sum_even =', sum_even,'  ', 'sum_odd =', sum_odd)
print('')
print(sorted(list_1)[-1])
print(list_1.index(sorted(list_1)[-1]))
