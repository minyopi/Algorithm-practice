from collections import deque

s = deque()
n = int(input())

for i in range(n):
    i = int(input())
    if i == 0:
        s.pop()
    else:
        s.append(i)

print(sum(s))