n = input()

if int(n) < 10:
        n = '0'+ n

x = n
count = 0


while True:
    x_list = [int(i) for i in x]
    x = str(x_list[-1]) + str(sum(x_list))[-1]
    count += 1
    if n == x:
        break

print(count)