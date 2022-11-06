list_1 = [32,43,1,3,4,5,34,5,1,7,10,34,17,11,32,43,1,3,4,5]
for i in range(0,len(list_1),5):
    list_1[i: i + 5] = sorted(list_1[i: i + 5], reverse=(i + 5) % 10 == 0)
print(list_1)
