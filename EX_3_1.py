message_1 = str(input())
message_2 = str(input())
message_3 = str(input())
for i in [message_1, message_2,message_3]:
    if len(i) % 2:
        print(i[len(i) // 2])
    else:
        print(i[len(i) // 2-1] + i[len(i) // 2])


