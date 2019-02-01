import math
from functools import reduce

n = int(input())
in_nums = list(map(int, input().split()))

max_prod = -math.inf
for i in range(n):
    for j in range(i, n):
        prod = reduce(lambda x, y: x * y, in_nums[i:j+1])
        if max_prod < prod:
            max_prod = prod

print(max_prod)
