def func():
    dt = {}
    while True:
        try:
            n = int(input())
            for i in range(n):
                x, y = map(int, input().split(' '))
                dt[x] = dt.get(x, 0) + y
            for i in sorted(dt.keys()):
                print(i, dt[i])
        except:
            break

func()
