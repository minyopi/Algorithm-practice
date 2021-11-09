n = 10000 - int(input())

coins = [ 10000, 1000, 100, 10, 1 ]
count = 0

for coin in coins:
    count = count + (n // coin)
    n = n % coin

print(count)