n = int(input())*2

n_list = [True] * n

m = int(n ** 0.5)
for i in range(2, m+1):
    if n_list[i] == True:
        for j in range(i+i, n ,i):
            n_list[j] = False
p_list = [i for i in range(2, n) if n_list[i] == True]
    
count = 0
for i in p_list:
    if n/2 <= i <= n:
        count+=1
if n == 2:
    count = 1

print(count)