#coding:utf-8
#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
#
# @param strs string字符串一维数组
# @return string字符串
#
class Solution:
    def longestCommonPrefix(self , strs ):
        # write code here
        if len(strs) == 0:
            return ''

        if len(strs) == 1:
            return strs[-1]

        res = ''

        for index,i in enumerate(strs[0]):
            for j in strs[1:]:
                if index >= len(j):
                    return res

                if i != j[index]:
                    return res

            res += i

        return res



str = ["abca","abc","abca","abc","abcc"]
#str = ["a","b"]

run = Solution()
res = run.longestCommonPrefix(str)
print(res)