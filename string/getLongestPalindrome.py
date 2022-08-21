# -*- coding:UTF-8 -*-
'''
NC17 最长回文子串
描述
对于一个字符串，请设计一个高效算法，计算其中最长回文子串的长度。
给定字符串A以及它的长度n，请返回最长回文子串的长度。

示例1
输入：
"abc1234321ab",12
返回值：7
'''

class Solution:
    def getLongestPalindrome(self, A, n):
        # write code here
        if n<2:
            return len(A)

        start,end,mxlen = 0,0,0

        dp = [[0]*n for _ in range(len(A))]

        for j in range(n):
            for i in range(j):
                dp[i][j] = (A[i] == A[j]) and ((j-i<2) | dp[i+1][j-1])
                if dp[i][j] and mxlen<j-i+1:
                    mxlen=j-i+1
                    start=i
                    end=j
            dp[j][j] = 1

        return len(A[start:end+1])

A = "abc1234321ab"
n = 12

run = Solution()
res =  run.getLongestPalindrome(A,n)
print (res)