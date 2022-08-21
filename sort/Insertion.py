import sys
class Solution:
    def Insertion(self , list):
        # write code here
        for i in range(len(list)):
            index = i
            value = list[i]

            j = i
            while j>0 and value < list[j]:
                index = j
                j = j - 1
            list[i] = list[index]
            list[index] = value

        return list

list = sys.argv[1]
list_int = [int(i) for i in list.split(",")]
r = Solution().Insertion(list_int)
print (r)