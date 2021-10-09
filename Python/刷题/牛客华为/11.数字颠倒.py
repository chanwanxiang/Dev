def func():
    """
    1. 切片
    2. 列表reverse方法
    3. 列表推导式
    4. 双指针
    """
    str = input()
    print(str[::-1])

    strs = list(str)
    strs.reverse()
    print(''.join(strs))

    strs = list(str)
    print(''.join(strs[-x] for x in range(1, len(strs)+1)))

    strs = list(str)
    i, j = 0, len(strs)-1
    while i < j:
        strs[i], strs[j] = strs[j], strs[i]
        i += 1
        j -= 1
    print(''.join(strs))
