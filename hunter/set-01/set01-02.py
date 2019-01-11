n = int(input())
nums = sorted(list(map(int, input().split())), reverse=True)

print("".join(map(str, nums)))
