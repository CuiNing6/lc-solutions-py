
# class Solution:
#     def spiralOrder(self , matrix ):
#         res = []
#         while matrix:
#             res += matrix[0]
#             matrix = list(zip(*matrix[1:]))[::-1]
#         return res



#
class Solution:
    def spiralOrder(self , matrix ):
        # write code here
        if matrix is None or matrix == []:
            return []

        top = 0
        left = 0
        right = len(matrix[0]) - 1
        bottom = len(matrix) - 1

        res = []

        while top <= len(matrix)//2 and left <= len(matrix[0])//2:
            if bottom < top or right < left:
                break

            for i in range(left, right+1):
                res.append(matrix[top][i])
            print (res)

            for i in range(top+1, bottom+1):
                res.append(matrix[i][right])

            tmp_right = right - 1
            for i in range(right):
                if top != bottom and i >= left:
                    res.append(matrix[bottom][tmp_right])
                    tmp_right = tmp_right - 1

            tmp_bottom = bottom - 1
            for i in range(bottom):
                if right != left and i >= top+1:
                    res.append(matrix[tmp_bottom][left])
                    tmp_bottom = tmp_bottom - 1
                print (res)


            left = left + 1
            right = right - 1
            top = top + 1
            bottom = bottom - 1

        return res


# matrix = [[1,2,3],[4,5,6],[7,8,9]]
matrix = [[2,5,8],[4,0,-1]]
run = Solution()
res =  run.spiralOrder(matrix)
print (res)