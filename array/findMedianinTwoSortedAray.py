# -*- coding:UTF-8 -*-
'''
在两个长度相等的排序数组中找到上中位数

描述
给定两个有序数组arr1和arr2，已知两个数组的长度都为N，求两个数组中所有数的上中位数。
上中位数：假设递增序列长度为n，若n为奇数，则上中位数为第n/2+1个数；否则为第n/2个数
[要求]
时间复杂度为O(logN)，额外空间复杂度为O(1)

输入：[1,2,3,4],[3,4,5,6]
返回值：3
说明：总共有8个数，上中位数是第4小的数，所以返回3。
'''
class Solution:
    def findMedianinTwoSortedAray(self , arr1 , arr2 ):
        # write code here
        if arr1 is None or arr2 is None or len(arr1)!=len(arr2):
            return False

        start1=0
        end1=len(arr1)-1

        start2=0
        end2=len(arr2)-1

        while start1<end1:
            mid1=(end1+start1)//2
            mid2=(end2+start2)//2

            if (end1-start1+1)%2 == 0:
                offset = 1
            else:
                offset = 0

            if arr1[mid1] > arr2[mid2]:
                end1=mid1
                start2=mid2+offset
            elif arr1[mid1] < arr2[mid2]:
                start1=mid1+offset
                end2=mid2
            else:
                return arr1[mid1]

        return min(arr1[start1],arr2[start2])


arr1 = [1,2,3,4]
arr2 = [3,4,5,6]
arr11=[0,1,2]
arr22=[3,4,5]

run = Solution()
res =  run.findMedianinTwoSortedAray(arr11,arr22)
print (res)