import math

n = int(input())
in_nums = list(map(int, input().split()))

max_sum = -math.inf
for i in range(n):
    for j in range(i, n):
        if max_sum < sum(in_nums[i:j+1]):
            max_sum = sum(in_nums[i:j+1])

print(max_sum)
