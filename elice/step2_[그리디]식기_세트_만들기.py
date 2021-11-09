C, S, E = map(int, input().split())


CC = C // 2
count_set = 0

if CC <= S :
    count_set = CC
elif CC > S:
    count_set = S

    
print(count_set)