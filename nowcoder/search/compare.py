#coding:utf-8
#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
# 比较版本号
# @param version1 string字符串
# @param version2 string字符串
# @return int整型
#
class Solution:
    def compare(self , version1 , version2 ):
        # write code here
        ver1 = version1.split(".")
        ver2 = version2.split(".")

        ver1_list = [int(x) for x in ver1]
        ver2_list = [int(x) for x in ver2]

        min_len = min(len(ver1_list), len(ver2_list))

        for i in range(min_len):
            if ver1_list[i] > ver2_list[i]:
                return 1
            elif ver1_list[i] < ver2_list[i]:
                return -1

        if len(ver1_list) == len(ver2_list):
            return 0
        elif len(ver1_list) > len(ver2_list):
            for j in range(len(ver2_list),len(ver1_list)):
                if ver1_list[j] > 0:
                    return 1
            return 0
        elif len(ver1_list) < len(ver2_list):
            for k in range(len(ver1_list),len(ver2_list)):
                if ver2_list[k] > 0:
                    return -1
            return 0

version1="1.1"
version2="1.1.1"
r = Solution()
res = r.compare(version1,version2)
print(res)