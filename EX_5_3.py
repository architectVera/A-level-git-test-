def check(document:str):
    s1="".join(c for c in document if c.isalpha()).lower()
    s2 = s1[::-1]
    return 'Паліндром' if s1[0: len(s1) // 2] == s2[0: len(s2) // 2] else 'Не паліндром'

check('І що салrо? Ласощі')





