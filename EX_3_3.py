message_1 = str(input())
if len(message_1) <= 10:
    message_2 = message_1[-3:].lower()
    message_3 = message_1[:-3]
    print(message_3[:len(message_3) // 2] + message_2 + message_3[len(message_3) // 2:])