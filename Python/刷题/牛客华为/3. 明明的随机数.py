def randomint():
    while True:
        try:
            n = int(input())
            sets = set()
            for i in range(n):
                sets.add(int(input()))
            nums = list(sets)
            nums.sort()
            for i in nums:
                print(i)
        except:
            break
