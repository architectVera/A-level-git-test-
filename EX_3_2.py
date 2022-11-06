message_1 = str(input())
if 5 <= len(message_1) <= 15:
    message_1 = message_1[len(message_1)-len(message_1) // 2:] + message_1[:len(message_1) // 2]
    print(message_1[:-3] + message_1[-3:].upper())