#coding:utf-8
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
#
# @param preOrder int整型一维数组
# @param vinOrder int整型一维数组
# @return TreeNode类
#
class Solution:
    def reConstructBinaryTree(self , preOrder , vinOrder ):
        # write code here
        if not preOrder and not vinOrder:
            return None

        root = TreeNode(preOrder[0])

        if set(preOrder) != set(vinOrder):
            return None

        i = vinOrder.index(preOrder[0])

        root.left = self.reConstructBinaryTree(preOrder[1:i+1],vinOrder[:i])
        root.right = self.reConstructBinaryTree(preOrder[i+1:],vinOrder[i+1:])

        return root


pre = [1, 2, 4, 7, 3, 5, 6, 8]
tin = [4, 7, 2, 1, 5, 3, 8, 6]

r = Solution()
res = r.reConstructBinaryTree(pre, tin)
print(res.val,res.left.val,res.left.left.val,res.left.left.right.val,res.right.val,res.right.left.val,res.right.right.val,res.right.right.left.val)