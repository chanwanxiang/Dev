def approximate():
    i, j = map(int, input().split('.'))
    print(i, j)
    if int(str(j)[0]) < 5:
        print(i)
    else:
        print(i+1)

approximate()


def func():
    num = float(input())
    res = num + 0.5
    print(int(res))


func()
