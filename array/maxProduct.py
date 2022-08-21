
class Solution:
    def maxProduct(self , arr ):
        # write code here
        if arr == None:
            return None

        res = min_tmp = max_tmp = arr[0]

        for i in range(1, len(arr)):
            if arr[i] > 0:
                max_tmp = max(arr[i], arr[i]*max_tmp)
                min_tmp = min(arr[i], arr[i]*min_tmp)
            else:
                max_tmp_tmp = max_tmp
                max_tmp = max(arr[i], arr[i]*min_tmp)
                min_tmp = min(arr[i], arr[i]*max_tmp_tmp)

            res = max(res, max_tmp)

        return res

# arr = [-2.5,4,0,3,0.5,8,-1]
arr = [0.1,0.0,3.0,-2.0,0.9,-1.3,5.0,-4.4]
run = Solution()
res =  run.maxProduct(arr)
print (res)