#coding:utf-8
#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
#
# @param n int整型 the n
# @return int整型
#
class Solution:
    def Nqueen(self , n ):
        # write code here
        if n == 1:
            return 1

        board = [['.' for _ in range(n)] for _ in range(n)]

        def check(board,row,col):
            for r in range(row):
                if board[r][col] == 'Q':
                    return False

            i, j = row, col
            while i>0 and j>0:
                if board[i-1][j-1] == 'Q':
                    return False
                i -= 1
                j -= 1

            i, j = row, col
            while i>0 and j<n-1:
                if board[i-1][j+1] == 'Q':
                    return False
                i -= 1
                j += 1

            return True

        res = []
        def dfs(r,res):
            if r == n:
                res.append(1)
                return

            for i in range(n):
                if check(board,r,i):
                    board[r][i] = 'Q'
                    dfs(r+1,res)
                    board[r][i] = '.'

        dfs(0,res)
        return sum(res)

n = 5
r = Solution()
res = r.Nqueen(n)
print(res)



