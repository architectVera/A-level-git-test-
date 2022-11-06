list_1 = [32,43,1,3,4,5,34,5,1,7,10,34,17,11,32,43,1,3,4,5]
list_2 = []
for i in range(0,len(list_1),5):
    if (i + 5) % 10 == 0:
         newlist = list_1[i: i + 5]
         newlist.sort(reverse=True)
         # print(newlist)
    else:
        newlist = list_1[i: i + 5]
        newlist.sort()
        # print(newlist)
    list_2 = list_2 + newlist
print(list_2)
