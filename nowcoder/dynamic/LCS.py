#coding:utf-8
#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
# longest common subsequence
# @param s1 string字符串 the string
# @param s2 string字符串 the string
# @return string字符串
#
class Solution:
    def LCS(self , s1 , s2 ):
        # write code here
        if s1 is None or s2 is None:
            return "-1"

        dict = [[0]*(len(s2)+1) for _ in range(len(s1)+1)]

        for i in range(1,len(s1)+1):
            for j in range(1,len(s2)+1):
                if s1[i-1] == s2[j-1]:
                    dict[i][j] = dict[i-1][j-1] + 1
                else:
                    dict[i][j] = max(dict[i-1][j],dict[i][j-1])

        l1 = len(s1)
        l2 = len(s2)

        s = []

        while dict[l1][l2] != 0:
            if dict[l1][l2] == dict[l1-1][l2]:
                l1 -= 1
            elif dict[l1][l2] == dict[l1][l2-1]:
                l2 -= 1
            elif dict[l1][l2] > dict[l1-1][l2-1]:
                l1 -= 1
                l2 -= 1
                s.append(s1[l1])

        res = ""

        while len(s) != 0:
            res += s[-1]
            s.pop()

        if res is None or res == "":
            return "-1"
        else:
            return res

    def LCS_v1(self, str1 , str2 ):
        if str1 is None or str2 is None:
            return ""

        dict = [[0]*(len(str2)+1) for _ in range(len(str1)+1)]
        max_num = 0
        pos = 0

        for i in range(1,len(str1)+1):
            for j in range(1,len(str2)+1):
                if str1[i-1] == str2[j-1]:
                    dict[i][j] = dict[i-1][j-1] + 1
                if dict[i][j] > max_num:
                    max_num = dict[i][j]
                    pos = i-1

        print(max_num,pos)

        return str1[pos-max_num+1:pos+1]

    def LCS_v2(self, str1, str2):
        if str1 is None or str2 is None:
            return ""

        res = ""
        max_len = 0

        if len(str1) < len(str2):
            str1, str2 = str2, str1

        for i in range(len(str1)):
            if str1[i-max_len:i+1] in str2:
                res = str1[i-max_len:i+1]
                max_len += 1

        return res



# s1 = "1A2C3D4B56"
# s2 = "B1D23A456A"
#
# r = Solution()
# res = r.LCS(s1,s2)
# print(res)

s1 = "22222"
s2 = "22222"

r = Solution()
res = r.LCS_v2(s1,s2)
print(res)