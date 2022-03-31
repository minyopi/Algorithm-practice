# 나의 답 첫번째 (15분 소요)
n = int(input())

count = 0

for x in range(60):
    for y in range(60):
        for z in range(0,n+1):
            if str(x).find('3') != -1 or str(y).find('3') != -1 or str(z).find('3') != -1:
                count += 1

print(count)


# 문제 풀이
# 문제풀이를 보면 나의 코드와 가독성이 다름.
# 받은 숫자는 시간이기 때문에 hour 로 표시하는것, 시분초 순서대로 코드를 짜는것.
h = int(input())

count = 0

for x in range(h+1):
    for y in range(60):
        for z in range(60):
            if '3' in str(x)+str(y)+str(z):
                count += 1

print(count)