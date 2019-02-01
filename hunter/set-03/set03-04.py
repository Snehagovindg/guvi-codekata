a, k = map(int, input().split())
in_nums = list(map(int, input().split()))

if k in in_nums:
    print('YES')
else:
    for i in range(a):
        s = 0
        for j in range(i, a):
            s += in_nums[j]
            if s > k:
                break
            elif s == k:
                print('YES')
                quit(0)
    print('NO')
