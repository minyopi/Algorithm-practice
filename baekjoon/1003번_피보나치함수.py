n = int(input())
n_List =  [int(input()) for _ in range(n)]


db = [ [] for _ in range(max(n_List)+1) ]
db[0] = [1,0]
db[1] = [0,1]

for i in range(2, max(n_List)+1):
    db[i] = [db[i-1][0] + db[i-2][0] , db[i-1][1] + db[i-2][1]]

for i in n_List:
    answer = []
    for j in db[i]:
        answer.append(str(j))
    print(" ".join(answer))