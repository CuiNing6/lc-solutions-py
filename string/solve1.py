# -*- coding:UTF-8 -*-
'''
NC1 大数加法
描述
以字符串的形式读入两个数字，编写一个函数计算它们的和，以字符串形式返回。
（字符串长度不大于100000，保证字符串仅由'0'~'9'这10种字符组成）

示例1
输入："1","99"
返回值："100"

说明：1+99=100
'''

# class Solution:
#     def solve(self , s , t ):
#         # write code here
#         mxlen = len(s) if len(s) > len(t) else len(t)
#
#         s = s.zfill(mxlen)
#         t = t.zfill(mxlen)
#
#         result = [0 for i in range(mxlen+1)]
#
#         s = list(s)
#         t = list(t)
#
#         for i in range(mxlen-1,-1,-1):
#             tmp = int(s[i]) + int(t[i]) + int(result[i+1])
#             print (s[i],t[i],result[i+1])
#             if tmp >= 10:
#                 result[i+1] = tmp % 10
#                 result[i] += tmp//10
#             else:
#                 result[i+1] = tmp
#
#             print (result)
#
#         if result[0] == 0:
#             res_tmp = result[1:]
#         else:
#             res_tmp = result
#
#         res = ''
#         for i in range(0,len(res_tmp)):
#             res += str(res_tmp[i])
#
#         return res

class Solution:
    def solve(self , s , t ):
        # write code here
        res = int(s) + int(t)

        return str(res)


s = "9"
t = "99999999999999999999999999999999999999999999999999999999999994"
#"100000000000000000000000000000000000000000000000000000000000003"

s2 = "733064366"
t2 = "459309139"
# "1192373505"

s1 = "1"
t1 = "99"
run = Solution()
res =  run.solve(s,t)
print (res)