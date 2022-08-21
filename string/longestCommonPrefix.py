# -*- coding:UTF-8 -*-
'''
NC55 最长公共前缀
描述
编写一个函数来查找字符串数组中的最长公共前缀。

输入：["abca","abc","abca","abc","abcc"]
返回值："abc"
'''


class Solution:
    def longestCommonPrefix(self , strs ):
        # write code here
        if strs is None:
            return ""

        minlen = len(strs[0])
        res = ''

        for k in strs:
            if len(k) < minlen:
                minlen = len(k)

        for i in range(minlen):
            tmp = ''
            for j in strs:
                tmp = tmp + j[i]

            count = tmp.count(strs[0][i])
            if count == len(strs):
                res = res + strs[0][i]
            else:
                break

        return res

strs = ["abca","abc","abca","abc","abcc"]
strs1 = ["flower","flow","flight"]

run = Solution()
res =  run.longestCommonPrefix(strs1)
print (res)