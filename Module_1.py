# # 1
# char_to_find = 'h'
# input_value = input()
#
# print(f"{input_value=}")
#
# if input_value.count(char_to_find) < 2:
#     print(f"String does not have two symbols {char_to_find}")
# else:
#     pos_first = input_value.find(char_to_find)
#     pos_last = input_value.rfind(char_to_find)
#     print(f"Reversed string between {char_to_find} = {input_value[pos_first+1:pos_last][::-1]}")
#
#
# # 2
# str_1 = '//LLOOab cde67890'
# final = [0,0,0,0]
# for x in str_1:
#     if x.isupper():
#         final[0] += 1
#     elif x.islower():
#         final[1] += 1
#     elif x.isdigit():
#         final[2] += 1
#     else:
#         final[3] += 1
# print(final)
#
#
#
# # 3
# s = 'wfuhw312mjs19sj1d04'
# b = []
# for i in s:
#     if i.isdigit():
#         b.append(int(i))
# print(b)
#
#
# # 4
# def maker(a:str):
#     return a.replace(' ', '',a.count(' ')- 1)
# print(maker('Simple, remove the spaces from the string'))
#
#
# # 5
# def maker_2(a:list):
#     return ' '.join(map(str,a))
#
# print(maker_2([32, 4.43, 'lister', False, None, [1,2,3,4]]))
#
#
# # 6
# dict_1 = {'Токио' : 'Япония', 'Асмэра': 'Эритрея', 'Асунсьон': 'Парагвай', 'Афины': 'Греция', 'Ашхабад' : 'Туркмения', 'Абу-Даби' : 'ОАЭ','Абуджа':'Нигерия', 'Аддис-Абеба':'Эфиопия', 'Аккра': 'Гана', 'Амстердам': 'Нидерланды'}
#
# stop_word = 'stop'
#
# while True:
#     user_input = input()
#     if user_input == stop_word:
#         break
#     for k in dict_1:
#         if k == user_input:
#             print(f'Це столиця країни {dict_1[k]}')
#             break
#     else:
#         print('Ні,на жаль, це не столиця!')
#
#
# # 7
test_data = {
    "apple" : ['malum', 'omum', 'popula'],
    'fruit' : ['baca', 'bacca', 'popum'],
    'punishment' : ['malum', 'multa'],
    'dog' : 'canina'
    }



def smart_add(dst_dict: dict, k: str, v: str):
    print(f"{dst_dict=}, {k=}, {v}")
    if not dst_dict.get(k): # new item
        dst_dict[k] = v # create new element and put value as a string
    else: # exists
        if type(dst_dict[k]) == str and dst_dict[k] != v: # key exist, it is string and a different one, need to convert to array
            dst_dict[k] = [dst_dict[k], v]
        elif v not in dst_dict[k]: # array, we need to make sure the same value is not there
            dst_dict[k].append(v)

reversed_dict = {}

for k, v in test_data.items():
    if type(v) == str:
        smart_add(reversed_dict, v, k)
    else:
        for i in v:
            smart_add(reversed_dict, i, k)

print(reversed_dict)

#
# # 8
# test_data = ["a", "ababab", "aabb", "abcabcabcabc", "abcabccba", "aaaa"]
#
# def isRepetative(s: str)->bool:
#     for l in range(1,len(s)):
#         split_result = s.split(s[0:l])
#         if all(a == '' for a in split_result):
#             return True
#     return False
#
#
# for t in test_data:
#     print(isRepetative(t))
#
#
# # 9 googled :)
# test_data = ['(){}[]', '([{}])', '(}', '[(])','[({})](]']
#
# def isValid( s: str ):
#     while True:
#         if '()' in s :
#             s = s.replace ( '()' , '' )
#         elif '{}' in s :
#             s = s.replace ( '{}' , '' )
#         elif '[]' in s :
#             s = s.replace ( '[]' , '' )
#         else :
#             return not s
#
# for t in test_data:
#     print(isValid(t))
#
#
# # 10
# filename = "file_1.txt"
# file_encoding = "Windows-1251"
#
# with open(filename, 'r', encoding=file_encoding) as f:
#     words = f.read().split()
#     longest_word = max(words, key=len)
# with open(filename, "a", encoding=file_encoding) as f:
#     f.write(longest_word.upper())


# a = {"key1":1}
#
#
# print(a.get("key2"))
