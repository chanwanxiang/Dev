def partitionStrs(strs):
    n = len(strs)
    if n <= 8:
        print(strs + (8-n)*'0')
    else:
        print(strs[:8])
        strs = strs[8:]
        partitionStrs(strs)

while True:
    try:
        strs = input()
        partitionStrs(strs)
    except:
        break
