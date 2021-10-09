def func():
    strs = []
    while True:
        try:
            n = int(input())
            for i in range(n):
                strs.append(input())
            strs.sort()
            for i in strs:
                print(i)
        except:
            break

func()
