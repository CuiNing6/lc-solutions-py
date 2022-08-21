import sys
class Solution:
    def Heap(self , list):
        # write code here

        def build(list, root, end):
            while True:
                child = root * 2 + 1
                if child > end:
                    return list

                if child+1 <= end and list[child+1] > list[child]:
                    child = child + 1

                if list[child] > list[root]:
                    list[root], list[child] = list[child], list[root]
                    root = child

                else:
                    return list


        n = len(list)
        root = n//2 - 1

        for i in range(root,-1,-1):
            list = build(list, i, n-1)

        for j in range(n-1,-1,-1):
            list[j], list[0] = list[0], list[j]
            list = build(list,0,j-1)

        return list



#[8,1,5,3,9,2]
list = sys.argv[1]
list_int = [int(i) for i in list.split(",")]
r = Solution().Heap(list_int)
print (r)