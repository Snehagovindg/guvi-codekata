n = int(input())
in_nums = list(map(int, input().split()))

result = []
j = 0
for i in range(n):
    result.append(1)
    for j in range(n):
        if i != j:
            result[i] *= in_nums[j]

print(*result)
