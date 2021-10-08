def func():
    strs = input()
    dt = {}
    for i in strs:
        dt[i] = dt.get(i, 0) + 1
    print(len(dt.keys()))

func()
