n = int(input())
nums = list(map(int, input().split()))

out = []

for i in range(n):
    if nums[i] == i:
        out.append(i)

if out:
    print(*sorted(out))
else:
    print('-1')
