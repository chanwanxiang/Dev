def func():
    n = int(input())
    strs = bin(n)
    dt = {}
    for i in strs:
        dt[i] = dt.get(i, 0) + 1
    return dt['1']

print(func())
