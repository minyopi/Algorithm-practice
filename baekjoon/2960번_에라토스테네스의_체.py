n, m = map(int, input().split())

def solution(n):
    count = 0
    n_list = [i for i in range(0,n+1)]

    for i in range(2, len(n_list)):
        if n_list[i] != 0:
            count += 1
            if count == m:
                return n_list[i]
            n_list[i] = 0
            for j in range(i+i, len(n_list) ,i):
                if n_list[j] != 0:
                    count += 1
                    if count == m:
                        return n_list[j]
                    n_list[j] = 0
    

print(solution(n))