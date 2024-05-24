#coding:utf-8
#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
#
# @param nums int整型一维数组
# @param target int整型
# @return int整型
#
class Solution:
    def search(self , nums , target ):
        # write code here
        if not nums:
            return -1

        left = 0
        right = len(nums)-1

        while left <= right:
            mid = left + (right - left) // 2

            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                right = mid - 1
            elif nums[mid] < target:
                left = mid + 1

        return -1

nums = [-1,0,3,4,6,10,13,14]
target = 3
r = Solution()
res = r.search(nums,target)
print(res)
