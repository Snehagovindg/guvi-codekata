n, q = map(int, input().split())

for i in range(n+1, q):
    if i % 2 == 1:
        print(i, end=' ')

print('\b')
