import sys
class Solution:
    def Shell(self , list):
        # write code here
        gap = len(list)//2

        while gap > 0:
            for i in range(gap,len(list)):
                tmp = list[i]
                j = i
                while j >= gap and list[j-gap] > tmp:
                    list[j] = list[j-gap]
                    j = j - gap

                list[j] = tmp

            gap = gap//2

        return list

list = sys.argv[1]
list_int = [int(i) for i in list.split(",")]
r = Solution().Shell(list_int)
print (r)


