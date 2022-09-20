# -*- coding:utf-8 -*-
'''
描述
给出两个字符串 s 和 t，要求在 s 中找出最短的包含 t 中所有字符的连续子串。

数据范围：0≤∣S∣,∣T∣≤10000，保证s和t字符串中仅包含大小写英文字母
要求: 时间复杂度 O(n)
例如：
S ="XDOYEZODEYXNZ"
T ="XYZ"
找出的最短子串为"YXNZ""YXNZ".

注意：
如果 s 中没有包含 t 中所有字符的子串，返回空字符串 “”；
满足条件的子串可能有很多，但是题目保证满足条件的最短的子串唯一。

示例1
输入："XDOYEZODEYXNZ","XYZ"
返回值："YXNZ"

示例2
输入："abcAbA","AA"
返回值："AbA"
'''
#
#
# @param S string字符串
# @param T string字符串
# @return string字符串
#
class Solution:
    def minWindow(self , S , T ):
        # write code here
        cnt = len(S) + 1

        hash = {}

        for i in T:
            if i not in hash:
                hash[i] = -1
            else:
                hash[i] -= 1

        slow = 0
        fast = 0
        left = -1
        right = -1

        while fast < len(S):
            if S[fast] in hash:
                hash[S[fast]] += 1

            while(self.check(hash)):
                if cnt > fast - slow + 1:
                    cnt = fast - slow + 1
                    left = slow
                    right = fast

                if S[slow] in hash:
                    hash[S[slow]] -= 1

                slow += 1

            fast += 1

        if left == -1:
            return ""

        return S[left:right+1]


    def check(self, dict):
        for key, value in dict.items():
            if value < 0:
                return False
        return True

S = "XDOYEZODEYXNZ"
T = "XYZ"
run = Solution()
res = run.minWindow(S, T)
print(res)