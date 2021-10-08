def func():
    num = int(input())
    res = 0
    while num:
        a = num % 10
        num = num // 10
        if str(a) not in str(res):
            res = res*10 + a
    print(res)

func()
