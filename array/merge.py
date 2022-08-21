
#
class Solution:
    def merge(self , A, m, B, n):
        # write code here
        if not A and not B:
            return []
        elif not A:
            return B
        elif not B:
            return A

        res = [0 for i in range(m+n)]

        while m > 0 and n > 0:
            if A[m-1] > B[n-1]:
                res[m+n-1] = A[m-1]
                m = m - 1
            else:
                res[m+n-1] = B[n-1]
                n = n - 1

        if n>0:
            res[:n] = B[:n]
        else:
            res[:m] = A[:m]

        return res

A = []
B = [1]
m = 0
n = 1
run = Solution()
res =  run.merge(A, m, B, n)
print (res)