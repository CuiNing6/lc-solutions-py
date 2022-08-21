# -*- coding:UTF-8 -*-
'''
Given a 2D board and a word, find if the word exists in the grid.
给定一个2维数组和一个单词，找到单词是否存在于2维数组中。
board =
[
['A','B','C','E'],
['S','F','C','S'],
['A','D','E','E']
]
Given word = "ABCCED", return true.
Given word = "SEE", return true.
Given word = "ABCB", return false

思路：每次遍历到错误的节点需要返回，最完美的解决办法就是回溯了，从每个节点出发判断上下左右四个节点是不是匹配word的下一个字母，如果匹配则继续dfs递归，不匹配或者超过边界则返回。
'''

class Solution:
    def exist(self, board, word):
        if word is None:
            return True
        if board is None:
            return False

        for i in range(len(board)):
            for j in range(len(board[0])):
                if self.dfs(i,j,board,word):
                    return True

        return False


    def dfs(self,i,j,board,word):
        if not word:
            return True
        if i<0 or i>=len(board) or j<0 or j>=len(board[0]) or board[i][j]!=word[0]:
            return False

        tmp = board[i][j]
        board[i][j] = '.'
        if self.dfs(i-1,j,board,word[1:]) or self.dfs(i+1,j,board,word[1:]) or self.dfs(i,j-1,board,word[1:]) or self.dfs(i,j+1,board,word[1:]):
            return True

        board[i][j] = tmp

        return False

board =[
['A','B','C','E'],
['S','F','C','S'],
['A','D','E','E']
]
word = "ABCCED"
word1 = "SEE"
word2 = "ABCB"
run = Solution()
res =  run.exist(board,word1)
print (res)
