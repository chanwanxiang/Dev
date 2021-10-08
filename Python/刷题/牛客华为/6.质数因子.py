def primeNum():
    n = int(input())
    i = 2
    while i*i <= n:
        while n % i == 0:
            n = n // i
            print(i, end=' ')
        i += 1
    if n - 1:
        print(n, end=' ')

primeNum()
