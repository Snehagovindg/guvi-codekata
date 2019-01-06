def is_prime(n):
    if n <= 3:
        return n > 1
    elif n%2 == 0 or n%3 == 0:
        return False

    i = 5
    while i*i <= n:
        if n%i == 0 or n%(i+2) == 0:
           return False
        i += 6
    return True


n, q = map(int, input().split())

for i in range(n+1, q):
    if is_prime(i):
        print(i, end=' ')
