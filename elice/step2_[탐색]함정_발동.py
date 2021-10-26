
place = list(input() for _ in range(8))
H_place = []

for i in range(0,8):
    for j in range(0,8):
        if place[i][j] == 'H':
            H_place.append([i,j])

trap = (['10101010']+['01010101'])*4
count = 0

for i in H_place:
    if trap[i[0]][i[1]] == '1':
        count += 1

print(count)