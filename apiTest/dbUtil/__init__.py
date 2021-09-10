class A:
    c, b = 2, 2
    ls = [[0 for i in range(c)] for j in range(b)]

A = A()
print(A.ls)
