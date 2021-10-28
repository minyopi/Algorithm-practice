n = int(input())
answer = 0
x = n

while x > 0:
    x_sum = 0
    x_List = []
    x = str(x)
    for i in x:
        x_List.append(int(i))
    x = int(x)
    x_sum = x + sum(x_List)
    if x_sum == n:
        answer = int(x)
        x -= 1
    else:
        x -= 1
        
print(answer)