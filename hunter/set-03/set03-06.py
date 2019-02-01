n = int(input())
in_nums = list(map(int, input().split()))

print(*in_nums[::-1], sep='->')
