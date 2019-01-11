n, q = map(int, input().split())
o = []
for i in range(n+1, q):
    if i % 2 == 1:
        o.append(i)

print(*o)
