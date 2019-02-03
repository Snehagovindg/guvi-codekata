n = int(input())

byes = 0

while n & n-1:
    n -= 1
    byes += 1

print(byes)
