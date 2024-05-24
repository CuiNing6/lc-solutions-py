# -*- coding:UTF-8 -*-
'''
描述
给出一个整型数组 numbers 和一个目标值 target，请在数组中找出两个加起来等于目标值的数的下标，返回的下标按升序排列。
（注：返回的数组下标从1开始算起，保证target一定可以由数组里面2个数字相加得到）

数据范围：2≤len(numbers)≤10^5
 ，-10 ≤numbersi≤10^9
 ，0 ≤target≤10^9

要求：空间复杂度 O(n)，时间复杂度 O(nlogn)

示例1
输入：[3,2,4],6
返回值：[2,3]
说明：
因为 2+4=6 ，而 2的下标为2 ， 4的下标为3 ，又因为 下标2 < 下标3 ，所以返回[2,3]

示例2
输入：[20,70,110,150],90
返回值：[1,2]
说明：20+70=90

@param numbers int整型一维数组
@param target int整型
@return int整型一维数组
'''
class Solution:
    def twoSum(self , numbers , target ):
        # write code here
        hash_res = {}
        res = []

        for i, j in enumerate(numbers):
            if j not in hash_res.keys():
                hash_res[target - j] = i
            else:
                res.extend([hash_res[j]+1, i+1])
                return res

numbers = [3,2,4]
run = Solution()
res = run.twoSum(numbers, 6)
print(res)







def again(numbers , target):
    if numbers is None:
        return []

    dict = {}
    res = []

    for i,num in enumerate(numbers):
        if target - num in dict.keys():
            res.extend([dict[target-num]+1,i+1])
        else:
            dict[num] = i

    return res

# numbers = [20,70,110,150]
# res = again(numbers, 90)
# print(res)




def again_v1(number, target):
    if numbers is None:
        return []

    res = []
    dict = {}

    for i, num in enumerate(number):
        if target - num in dict:
            res.extend([dict[target-num]+1,i+1])
        else:
            dict[num] = i

    return res

# numbers = [20,70,110,150]
# res = again_v1(numbers, 90)
# print(res)




def nSum(arr,n,start,target):
    if not arr:
        return None

    res = []

    if n == 2:
        dict = {}
        for i in range(start,len(arr)):
            if target - arr[i] in dict:
                tmp = [target-arr[i],arr[i]]
                tmp.sort()
                if tmp not in res:
                    res.append(tmp)
            else:
                dict[arr[i]] = i
        res.sort()
    else:
        for j in range(start,len(arr)):
            res_pre = nSum(arr,n-1,j+1,target-num[j])
            if res_pre != None:
                for k in res_pre:
                    k.append(arr[j])
                    k.sort()
                    if k not in res:
                        res.append(k)
        res.sort()

    return res
#
# num = [-10,0,10,20,-10,-40]
# numbers = [20,70,110,150]
# print("num:",num)
# print("numbers",numbers)
#
# # res = nSum(num,4,0,20)
# res = nSum(numbers,2,0,90)
# print(res)








def again_0219(arr,k):
    if not arr:
        return

    res = []
    dict = {}

    for i,num in enumerate(arr):
        if k-num in dict:
            res.extend([dict[k-num]+1,i+1])
        else:
            dict[num] = i

    return res

# numbers = [20,70,110,150]
# res = again_0219(numbers, 90)
# print(res)


def again_0219_three(arr):
    if not arr:
        return

    res = []

    for i in range(len(arr)):
        dict = {}
        for j in range(i+1,len(arr)):
            target = -arr[i] - arr[j]
            if target in dict:
                tmp = [arr[i],arr[j],target]
                tmp.sort()
                if tmp not in res:
                    res.append(tmp)
            else:
                dict[arr[j]] = j

    res.sort()
    return res

# num = [-10,0,10,20,-10,-40]
# res = again_0219_three(num)
# print(res)
















