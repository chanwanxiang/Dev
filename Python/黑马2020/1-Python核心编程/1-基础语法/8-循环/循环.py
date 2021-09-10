# 循环

# 1)九九乘法表

row = 1

while row <= 9:
    col = 1
    while col <= row:
        print('%d*%d=%d'%(col, row, row*col), end=' ')
        col += 1
    # 换行
    print()
    row += 1
