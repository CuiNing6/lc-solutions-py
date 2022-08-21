import sys
class Solution:
    def Quick(self , list):
        # write code here
        left = 0
        right = len(list)-1
        res = self.sort(list, left, right)

        return res

    def sort(self, list, left, right):
        if left > right:
            return list

        low = left
        high = right
        key = list[left]

        while left < right:
            while left < right and list[right] > key:
                right = right - 1
            list[left] = list[right]

            while left < right and list[left] < key:
                left = left + 1
            list[right] = list[left]

        list[right] = key
        self.sort(list,low,left-1)
        self.sort(list,left+1, high)

        return list

# list = [9,6,8,5,7,4,2,0,1,3]

list = sys.argv[1]
list_int = [int(i) for i in list.split(",")]
r = Solution().Quick(list_int)
print (r)