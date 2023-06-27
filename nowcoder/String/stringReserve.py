#coding:utf-8
#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
#
# @param s string字符串
# @param n int整型
# @return string字符串
#
class Solution:
    def trans(self , s , n ):
        # write code here
        if n == 0:
            return s

        res = ''

        for i in range(n):
            if s[i] >= 'A' and s[i] <= 'Z':
               res += chr(ord(s[i]) - ord('A') + ord('a'))
            elif s[i] >= 'a' and s[i] <= 'z':
                res += chr(ord(s[i]) - ord('a') + ord('A'))
            else:
                res += s[i]

        res = list(res.split(' '))[::-1]

        return ' '.join(res)

    def trans_v1(self , s , n ):
        # write code here
        if n == 0:
            return s

        res = ''

        line = s.split(' ')

        for i in line:
            tmp = ''
            for j in i:
                if j.isupper():
                    tmp += j.lower()
                else:
                    tmp += j.upper()

            res = tmp + ' ' + res

        return res[0:n]


    def trans_v2(self , s , n):
        # write code here
        line = s.split(' ')
        line=line[::-1]
        s=""
        for word in line:
            word=word.swapcase()
            s+=word
            s+=" "
        return s[0:n]


s = "This is a sample"
n = 16

run = Solution()
res = run.trans_v2(s, n)
print(res)

