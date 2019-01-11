import collections as col

n = int(input())
nums = list(map(int, input().split()))
c = col.Counter(nums)
o = {k for k, v in c.items() if v > 1}

if o:
    for i in o:
        print(*o)
else:
    print('unique')
