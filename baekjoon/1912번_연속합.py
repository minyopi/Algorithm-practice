n = int(input())
nums = list(map(int, input().split(" ")))

def makeMaxNumber(nums):
    dp = [0 for _ in range(len(nums))]
    dp[0] = nums[0]

    for i in range(1,len(nums)):
        if nums[i] > dp[i-1] + nums[i]:
            dp[i] = nums[i]
        else:
            dp[i] = dp[i-1] + nums[i]

    return max(dp)

print(makeMaxNumber(nums))