# 나의 답 첫번째 (18분 소요)
# 시간이 많이 소요, result를 굳이 리스트로 설정해서 시간복잡도를 늘릴 필요가 없다.
n = int(input())
data = input().split()

result = [1,1]

for item in data:
    if item == 'R':
        result[1] += 1
    elif item == 'L':
        if result[1] > 1:
            result[1] -= 1
    elif item == 'U':
        if result[0] > 1:
            result[0] -= 1
    elif item == 'D':
        result[0] += 1

print(" ".join(list(map(str, result))))


# 문제 풀이 보고 개선
n = int(input())
data = input().split()

x,y = 1,1

for item in data:
    if item == 'R':
        y += 1
    elif item == 'L':
        if y > 1:
            y -= 1
    elif item == 'U':
        if x > 1:
            x -= 1
    elif item == 'D':
        x += 1

print(x,y)


# 문제 풀이
n = int(input())
plans = input().split()

x, y = 1,1

dx = [0,0,-1,1]
dy=[-1,1,0,0]
move_types=['L','R','U','D']

for plan in plans:
    for i in range(len(move_types)):
        if plan == move_types[i]:
            nx = x + dx[i]
            ny = y + dy[i]
    
    if nx <1 or ny<1 or nx > n or ny >n:
        continue
    x,y = nx, ny

print(x,y)