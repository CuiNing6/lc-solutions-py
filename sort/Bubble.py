import sys
class Solution:
    def Bubble(self , list ):
        # write code here
        for i in range(len(list)-1,1,-1):
            for j in range(i):
                if list[j] > list[j+1]:
                    tmp = list[j]
                    list[j] = list[j+1]
                    list[j+1] = tmp

        return list

# list = [9,6,8,5,7,4,2,0,1,3]
list = sys.argv[1]
list_int = [int(i) for i in list.split(",")]
r = Solution().Bubble(list_int)
print (r)


