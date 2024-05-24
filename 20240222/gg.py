

def sum_nums(nums):
    if not nums:
        return

    dp = [0]*(len(nums)+1)

    for i in range(1,len(nums)+1):
        dp[i] = max(dp[i-1]+nums[i-1],dp[i-1])


    return dp[len(nums)]


nums = [1,2,4,5,-1]
r = sum_nums(nums)
print(r)