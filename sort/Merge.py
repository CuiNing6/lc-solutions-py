import sys
class Solution:
    def Merge(self , list):
        # write code here
        if len(list) <= 1:
            return list

        mid = len(list)//2

        left = self.Merge(list[:mid])
        right = self.Merge(list[mid:])

        return self.sort(left, right)

    def sort(self, left, right):
        res = []
        i = 0
        j = 0

        while i < len(left) and j < len(right):
            if left[i] > right[j]:
                res.append(right[j])
                j = j + 1
            else:
                res.append(left[i])
                i = i + 1

        if i == len(left):
            res.extend(right[j:])
        else:
            res.extend(left[i:])

        return res

list = sys.argv[1]
list_int = [int(i) for i in list.split(",")]
print(list_int)
r = Solution().Merge(list_int)
print (r)