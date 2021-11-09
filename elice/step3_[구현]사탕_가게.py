n = int(input())

n_max = n

while n != 1:
    if n % 2 == 0:
        n = n // 2
        if n_max <= n:
            n_max = n
    else:
        n = n * 3 + 1
        if n_max <= n:
            n_max = n

print(n_max)