# 나의 답 첫번째 (10분 소요)
n,m = map(int, input().split())
dataList = [ sorted(list(map(int,input().split()))) for _ in range(n) ]

answer = dataList[0][0]

for data in dataList:
    if answer < data[0]:
        answer = data[0]

print(answer)


# 문제 해설 읽고 응용
n,m = map(int, input().split())
dataList = [ list(map(int,input().split())) for _ in range(n) ]

answer = 0

for data in dataList:
    min_num = min(data)
    answer = max(answer, min_num)

print(answer)

# 문제 해설 (1)
n,m = map(int, input().split())

result = 0

for i in range(n):
    data = list(map(int, input().split()))
    min_value = min(data)
    result = max(min_value, result)

# 문제 해설 (2)
n,m = map(int, input().split())

result = 0

for i in range(n):
    data = list(map(int, input().split()))
    min_value = 10001
    for j in data:
        min_value = min(min_value,a)
    result = max(result, min_value)

print(result)
