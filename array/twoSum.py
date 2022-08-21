
class Solution:
    def twoSum(self , numbers , target ):
        # write code here
        hashmap = {}
        res = []

        for i in range(len(numbers)):
            hashmap[numbers[i]] = i

        for j in range(len(numbers)):
            if target - numbers[j] in hashmap:
                if hashmap[target - numbers[j]] != j:
                    res.append(j+1)
                    res.append(hashmap[target-numbers[j]] + 1)

                    return res

        return res

numbers = [3,2,4]
target = 6
run = Solution()
res =  run.twoSum(numbers , target)
print (res)