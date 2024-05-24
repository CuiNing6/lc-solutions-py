#coding:utf-8
#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
#
# @param nums int整型一维数组
# @return int整型
#
class Solution:
    def findPeakElement(self , nums ):
        # write code here
        left = 0
        right = len(nums) - 1

        while left < right:
            mid = left + (right - left) // 2

            if nums[mid] > nums[mid+1]:
                right = mid
            elif nums[mid] < nums[mid+1]:
                left = mid + 1

        return right

nums = [1,2,3,1]
r = Solution()
res = r.findPeakElement(nums)
print(res)



def findleftbound(nums,target):
    left = 0
    right = len(nums) - 1

    while left <= right:
        mid = left + (right - left) // 2

        if nums[mid] == target:
            right = mid - 1
        elif nums[mid] > target:
            right = mid - 1
        elif nums[mid] < target:
            left = mid + 1

    if left >= len(nums) or nums[left] != target:
        return -1

    return left

# nums = [1,2,2,2,3]
# res = findleftbound(nums,2)
# print(res)


def findrightbound(nums,target):
    left = 0
    right = len(nums) - 1

    while left <= right:
        mid = left + (right - left) // 2

        if nums[mid] == target:
            left = mid + 1
        elif nums[mid] > target:
            right = mid - 1
        elif nums[mid] < target:
            left = mid + 1

    if right >= len(nums) or nums[right] != target:
        return -1

    return right

# nums = [1,2,2,2,3]
# res = findrightbound(nums,2)
# print(res)



def findnum(nums,target):
    left = 0
    right = len(nums) - 1

    while left <= right:
        mid = left + (right - left) // 2

        if nums[mid] == target:
            return mid
        elif nums[mid] > target:
            right = mid - 1
        elif nums[mid] < target:
            left = mid + 1

    return -1

# nums = [1,2,3]
# res = findnum(nums,3)
# print(res)
