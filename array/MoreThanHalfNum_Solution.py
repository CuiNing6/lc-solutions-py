# -*- coding:utf-8 -*-
class Solution:
    def MoreThanHalfNum_Solution(self, numbers):
        # write code here
        vote = 0
        res = 0

        for i in range(len(numbers)):
            if vote == 0:
                res = numbers[i]
                vote = vote + 1
            else:
                if numbers[i] == res:
                    vote = vote + 1
                else:
                    vote = vote - 1

        tmp = 0
        for i in range(len(numbers)):
            if numbers[i] == res:
                tmp = tmp + 1
            if tmp > len(numbers) / 2:
                return res

        return 0

numbers = [1,2,3,2,2,2,5,4,2]
run = Solution()
res =  run.MoreThanHalfNum_Solution(numbers)
print (res)