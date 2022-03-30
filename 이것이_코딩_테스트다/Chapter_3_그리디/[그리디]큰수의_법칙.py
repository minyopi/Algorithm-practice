# 나의 답 첫번째 (10분 소요)
N, M, K = map(int, input().split( ))
numList = sorted(list(map(int, input().split( ))),reverse=True)

answer = 0

for i in range(M):
    if i % N == 0:
       answer += numList[1]
    else:
        answer += numList[0]

print(answer)

# 문제 해설 읽고 응용
n,m,k = map(int, input().split())
data = list(map(int, input().split()))

data.sort()
first = data[-1]
seconf = data[-2]

answer = (m//k)*(first*k+second) + (m%(k+1))*first

print(answer)


# 문제 해설 (1)
import time
start_time = time.time()

n, m, k = map(int, input().split())
data = list(map(int, input().split()))

data.sort()
first = data[n-1]
second = data[n-2]

result = 0

while True:
    for i in range(k):
        if m == 0:
            break
        result += first
        m -= 1
    if m == 0:
        break
    result += second
    m -= 1

print(result)

end_time = time.time()
print("time: ", end_time - start_time)

# 문제 해설 (2)
n,m,k = map(int, input().split())
data = list(map(int, input().split()))

data.sort()
first = data[-1]
second = data[-2]

count = int(m / (k+1)) * k
count += m % (k+1)

result = 0
result += (count) * first
result += (m - count) * second

print(result)
