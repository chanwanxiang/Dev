def strlen():
    strs = input()
    strslist = strs.split(' ')
    if 0 < len(strs) < 5000:
        return len(strslist[-1])
    return -1
