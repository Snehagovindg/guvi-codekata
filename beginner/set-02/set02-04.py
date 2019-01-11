n, q = map(int, input().split())
odd = []
for i in range(n+1, q):
    if i % 2 == 1:
        odd.append(i)

print(*odd)
