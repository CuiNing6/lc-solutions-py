
class Solution:
    def maxProfit(self , prices ):
        # write code here
        if prices is None or len(prices) == 0:
            return None

        nobuy = 0
        buy = -prices[0]

        for i in range(1, len(prices)):

            nobuy = max(nobuy, buy+prices[i])
            buy = max(buy, -prices[i])

        return nobuy


# prices = [1,4,2]
# prices = [2,4,1]
# prices = [1]
prices = [1,2]
run = Solution()
res =  run.maxProfit(prices)
print (res)