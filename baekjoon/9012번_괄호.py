from collections import deque

def isVPS(PS):
    d = deque()

    for i in PS:
        if i == '(':
            d.append(i)
        else:
            if len(d) == 0:
                return 'NO'
            else:
                d.pop()
    if len(d) == 0:
        return 'YES'
    else:
        return 'NO'


n = int(input())
nList = [list(input()) for _ in range(n)]

for i in nList:
    print(isVPS(i))