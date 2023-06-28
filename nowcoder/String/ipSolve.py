#coding:utf-8
#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
# 验证IP地址
# @param IP string字符串 一个IP地址字符串
# @return string字符串
#
class Solution:
    def solve(self , IP ):
        # write code here
        if ":" in IP:
            lines = IP.split(':')
            if len(lines) != 8:
                return "Neither"
            for i in lines:
                if len(i) > 4 or i == '' or i == '00' or i == '000' or i == '0000':
                    return "Neither"
                for j in i:
                    if str.isnumeric(j):
                        if int(j) < 0 or int(j) > 9:
                            return "Neither"
                    if j.isupper():
                        if j < 'A' or j > 'F':
                            return "Neither"
                    if j.islower():
                        if j < 'a' or j > 'f':
                            return "Neither"
            return 'IPv6'

        elif "." in IP:
            lines = IP.split('.')
            if len(lines) != 4:
                return "Neither"
            for i in lines:
                if i == '' or str.isnumeric(i) == False:
                    return "Neither"
                if int(i) > 255 or int(i) < 0:
                    return "Neither"
                if int(i) > 0 and i[0] == '0':
                    return "Neither"
            return "IPv4"
        else:
            return "Neither"



#IP = "172.016.254.1"
IP = "20EE:FGb8:85a3:0:0:8A2E:0370:7334"

run = Solution()
res = run.solve(IP)
print(res)