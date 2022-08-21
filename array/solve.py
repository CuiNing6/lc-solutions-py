
# class Solution:
#     def solve(self , a ):
#         # write code here
#         if a is None:
#             return None
#
#         n = len(a)
#         index = len(a) / 2
#         tmp = a[len(a) / 2]
#         while n>0:
#             if tmp == index:
#                 a = a[len(a)/2:]
#                 n = len(a)
#                 index = len(a) / 2 + tmp
#                 tmp = a[len(a) / 2]
#             elif tmp > index:
#                 if a[len(a)/2 - 1] == index-1:
#                     return tmp - 1
#
#                 a = a[:len(a)/2]
#                 index = index - len(a)/2
#                 tmp = a[len(a)/2]
#                 n = len(a)
#
#             elif tmp <= index:
#                 if a[len(a) / 2 + 1] == index + 1:
#                     return tmp + 1
#                 a = a[len(a) / 2:]
#                 index = index + len(a) / 2
#                 tmp = a[len(a)/2]
#                 n = len(a)


class Solution:
    def solve(self , a ):
        # write code here
        if a is None:
            return None

        right = len(a) - 1
        left = 0
        while right >= left:
            mid = left + (right - left)//2
            if a[mid] == mid:
                left = mid + 1
            else:
                right = mid - 1

        return left



# a = [0,1,2,3,4,5,7]
# a = [0,2,3]
# a = [0,1,2,3,4,5,7,8]
a = [0,1,2,3,4,5,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28]
run = Solution()
res =  run.solve(a)
print (res)