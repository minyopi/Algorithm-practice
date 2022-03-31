# 나의 답 첫번째 (20분 소요)
x,y = input()

toInt = {"a":1,"b":2,"c":3,"d":4, "e":5,"h":6,"g":7,"h":8}
x = toInt[x]
y = int(y)

count = 0

nx = [2,1,-1,1,-2,-1,-2,-1]
ny = [1,2,1,-2,-1,-2,1,2]

for i in range(len(nx)):
    a = x
    b = y
    a += nx[i]
    b += ny[i]
    if a > 0 and b > 0 and a < 9 and b < 9:
        count+=1

print(count)

# 문제 해설
# 숫자를 int로 바꾸는데 유니코드로 바꾸는 메소드 ord() 를 사용!
# 변수명도 가독성이 좋게 설정

input_data = input()
row = int(input_data[1])
column = int(ord(input_data[0])) - int(ord("a")) + 1

steps = [(-2,-1),(-1,-2),(1,-2),(2,-1),(2,1),(1,2),(-1,2),(-2,1)]

result = 0

for step in steps:
    next_row = row + step[0]
    next_column = column + step[1]

    if next_row >= 1 and next_row <=8 and next_column >=1 and nexr_ column <= 8:
        result += 1

print(result)