import collections as col

nums = list(map(int, input().split()))
c = col.Counter(nums)
o = {k for k, v in c.items() if v > 1}

if o:
    for i in o:
        print(i, end=' ')
else:
    print('Unique')
