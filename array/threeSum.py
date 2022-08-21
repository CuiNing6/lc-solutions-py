
class Solution:
    def threeSum(self , num ):
        # write code here
        if num is None or len(num) < 3:
            return []

        res = []
        num = sorted(num)

        for i in range(len(num)-2):
            if num[i] > 0:
                break

            if i>0 and num[i] == num[i-1]:
                continue

            left = i + 1
            right = len(num)-1

            while left < right:
                sum = num[i] + num[left] + num[right]
                if sum == 0:
                    list = []
                    list.append(num[i])
                    list.append(num[left])
                    list.append(num[right])
                    res.append(list)

                    while left < right and num[left] == num[left + 1]:
                        left = left + 1
                    while left < right and num[right] == num[right - 1]:
                        right = right - 1

                    left = left + 1
                    right = right - 1

                elif sum > 0:
                    right = right - 1
                elif sum < 0:
                    left = left + 1

        return res

num = [-2,0,1,1,2]
# num = [-1,1,0]
run = Solution()
res =  run.threeSum(num)
print (res)

