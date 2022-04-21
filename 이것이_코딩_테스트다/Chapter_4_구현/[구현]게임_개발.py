# 나의 답 첫번째 (첫번째 시도 실패)(두번째 시도 1시간)
n,m = map(int, input().split())
now_n, now_m, d = map(int, input().split())
map_data = [ list(map(int,input().split())) for _ in range(m) ]

is_visited = [ [0 for _ in range(n)] for _ in range(m) ]
is_visited[now_n][now_m] = 1

answer = 1

def turn_left():
    global d
    d -= 1
    if d == -1:
        d = 3

dn = [0, 0, -1, 1]
dm = [-1, 1, 0, 0]

count_d = 0

while True:
    temp_n = now_n + dn[d]
    temp_m = now_m + dm[d]

    if is_visited[temp_n][temp_m] == 1 or map_data[temp_n][temp_m] == 1:
        if count_d == 4:
            count = 0
            for i in range(4):
                turn_left()
                if is_visited[temp_n][temp_m] == 1:
                    now_n = temp_n
                    now_m = temp_m
                count += 1
            if count == 4:
                break
                

    if is_visited[temp_n][temp_m] == 0 and map_data[temp_n][temp_m] == 0:
        now_n = temp_n
        now_m = temp_m
        count_d = 0
        is_visited[now_n][now_m] = 1
        answer += 1

    turn_left()
    count_d += 1

print(answer)


# # 문제 해설
n,m = map(int,input().split())
x,y,direction = map(int, input().split())

d = [[0] * m for _ in range(n)]
d[x][y] = 1

array = [list(map(int, input().split())) for _ in range(n)]

dx = [-1,0,1,0]
dy = [0,1,0,-1]

def turn_left():
    global direction
    direction -= 1
    if direction == -1:
        direction = 3

count = 1
turn_time = 0
while True:
    turn_left()
    nx = x + dx[direction]
    ny = y + dy[direction]
    
    if d[nx][ny] == 0 and array[nx][ny] == 0:
        d[nx][ny] = 1
        x = nx
        y = ny
        count += 1
        turn_time = 0
        continue
    else:
        turn_time += 1
    
    if turn_time == 4:
        nx = x - dx[direction]
        ny = y - dy[direction]
        if array[nx][ny] == 0:
            x = nx
            y = ny
        else:
            break
        turn_time = 0
    

print(count)