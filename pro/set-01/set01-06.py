n = int(input())
in_nums = list(map(int, input().split()))

result = []
for i in range(n-2):
    for j in range(i+1, n-1):
        for k in range(j+1, n):
            if in_nums[i] < in_nums[j] < in_nums[k]:
                result.append((in_nums[i], in_nums[j], in_nums[k], ))

print(len(result))
