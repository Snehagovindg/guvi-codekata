n, k = map(int, input().split())

in_sets = []

for _ in range(n):
    in_set = set(map(int, input().split()))
    in_sets.append(in_set)

out_list = set.intersection(*in_sets)

print(*out_list)
