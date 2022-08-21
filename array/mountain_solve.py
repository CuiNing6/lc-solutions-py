
class Solution:
    def solve(self , a ):
        # write code here
        if a is None or len(a) < 2:
            return 0

        n = len(a)-1

        while n>=0:
            if n == len(a)-1:
                if a[n] > a[n-1]:
                    return n
            elif n == 0:
                if a[n] > a[n+1]:
                    return n
            else:
                if a[n] > a[n-1] and a[n] > a[n+1]:
                    return n
            n = n - 1

        return 0

a = [2,4,1,2,7,8,4]
run = Solution()
res =  run.solve(a)
print (res)