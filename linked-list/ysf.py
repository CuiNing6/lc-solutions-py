
class Solution:
    def ysf(self , n , m ):
        # write code here
        if n<1 or m<1:
            return None

        res = []
        for i in range(n):
            res.append(i+1)

        k = 0
        for j in range(n-1):
            k = (k+m-1)%(n-j)
            del res[k]

        return res[0]

run = Solution()
l =  run.ysf(5, 2)
print (l)