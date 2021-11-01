R = int(input())

def prime_number(n):
    n_list = [True] * (n+1)

    m = int(n ** 0.5)
    for i in range(2, m+1):
        if n_list[i] == True:
            for j in range(i+i, n+1 ,i):
                n_list[j] = False
    p_list = [i for i in range(2, n+1) if n_list[i] == True]

    if n in p_list:
        return True
    else:
        return False
    

def solution(R):
    
    # 상대방의 숫자 구하기
    c = []
    for i in range(1,len(str(R))+1):
        c_str = str(R)[-i]
        if c_str == '1' or c_str == '0' or c_str == '2' or c_str == '5' or c_str == '8':
            c.append(c_str)
        elif c_str == '6':
            c.append('9')
        elif c_str == '9':
            c.append('6')

    C = int("".join(c))
    
    if len(str(C)) != len(str(R)):
        return 'no'
    
    # 소수 판별하기
    isR = prime_number(R)
    isC = prime_number(C)
    
    if isR == True and isC == True:
        return 'yes'
    else:
        return 'no'


print(solution(R))
