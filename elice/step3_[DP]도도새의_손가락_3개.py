N = int(input())

dp = [0 for _ in range(N+1)]
dp[1] = 1
dp[2] = 2
dp[3] = 4

for i in range(4, N+1):
    dp[i] = dp[i-1] + dp[i-2] +dp[i-3] 
    dp[i] = dp[i] % 123456  # 내가 놓친 부분! 여기서 123456으로 나눠주면 시간 단축 가능!

print(dp[N])