def func():
    strs = input().split(';')
    orig = [0, 0]
    for i in strs:
        if len(i) < 2 or i[0] not in ['A', 'D', 'S', 'W'] or not i[1:].isdigit():
            continue
        elif i[0] == 'A':
            orig[0] -= int(i[1:])
        elif i[0] == 'D':
            orig[0] += int(i[1:])
        elif i[0] == 'S':
            orig[1] -= int(i[1:])
        elif i[0] == 'W':
            orig[1] += int(i[1:])
    
    return f'{orig[0]},{orig[1]}'

print(func())
