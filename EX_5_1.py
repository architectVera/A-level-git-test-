def fun_1(sp:list, index_first:int, index_second:int):
    sp[ index_first:index_second] = sorted(sp[ index_first:index_second])
    return sp


fun_1([1,10,9,4,5,7,2,0], 2, 6)
print(fun_1)