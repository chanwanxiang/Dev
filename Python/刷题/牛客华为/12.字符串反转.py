def reverseStrs():
    strs = input()
    if not strs.islower and len(strs) > 1000:
        return -1
    return strs[::-1]

print(reverseStrs())
