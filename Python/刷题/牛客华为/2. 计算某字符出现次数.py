def countChar():
    strs, char = input(), input()
    chardict = {}
    for i in strs:
        chardict[i] = chardict.get(i, 0) + 1
    if char in chardict:
        return chardict[char]
    return -1
