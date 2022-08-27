# -*- coding:utf-8 -*-
'''
描述
给出一个有序的整数数组 A 和有序的整数数组 B ，请将数组 B 合并到数组 A 中，变成一个有序的升序数组

数据范围： 0≤n,m≤100，|A_i| <=100，|B_i| <= 100

注意：
1.保证 A 数组有足够的空间存放 B 数组的元素， A 和 B 中初始的元素数目分别为 m 和 n，A的数组空间大小为 m+n
2.不要返回合并的数组，将数组 B 的数据合并到 A 里面就好了，且后台会自动将合并后的数组 A 的内容打印出来，所以也不需要自己打印
3. A 数组在[0,m-1]的范围也是有序的

示例1
输入：[4,5,6],[1,2,3]
返回值：[1,2,3,4,5,6]
说明：A数组为[4,5,6]，B数组为[1,2,3]，后台程序会预先将A扩容为[4,5,6,0,0,0]，B还是为[1,2,3]，m=3，n=3，传入到函数merge里面，然后请同学完成merge函数，
    将B的数据合并A里面，最后后台程序输出A数组

示例2
输入：[1,2,3],[2,5,6]
返回值：[1,2,2,3,5,6]
'''

#
#
# @param A int整型一维数组
# @param B int整型一维数组
# @return void
#
class Solution:
    def merge(self , A, m, B, n):
        # write code here
        res = []

        i, j = 0, 0

        while i <= m - 1 and j <= n - 1:
            if A[i] > B[j]:
                res.append(B[j])
                j += 1
            else:
                res.append(A[i])
                i += 1

        if i<=m-1:
            res.extend(A[i:])
        else:
            res.extend(B[j:])

        return res

A = [4,5,6]
m = 3
B = [1,2,3]
n = 3

run = Solution()
res = run.merge(A,m,B,n)
print(res)



