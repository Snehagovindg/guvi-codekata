n, k = map(int, input().split())

in_nums = list(map(int, input().split()))

for i in range(k):
    for j in range(i, n):
        if in_nums[i] < in_nums[j]:
            in_nums[i], in_nums[j] = in_nums[j], in_nums[i]

print(in_nums[k-1])
