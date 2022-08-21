import sys
class Solution:
    def Selection(self , list ):
        # write code here
        tmp, min = 0, 0
        for i in range(len(list)):
            min = i
            for j in range(i,len(list)):
                if list[j] < list[min]:
                    min = j

            if i != min:
                tmp = list[i]
                list[i] = list[min]
                list[min] = tmp

        return list

#[8,1,5,3,9,2]
list = sys.argv[1]
list_int = [int(i) for i in list.split(",")]
r = Solution().Selection(list_int)
print (r)