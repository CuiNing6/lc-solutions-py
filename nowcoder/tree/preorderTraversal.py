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
# @param root TreeNode类
# @return int整型一维数组
#
class Solution:
    def preorderTraversal(self , root ):
        # write code here

        res = []

        def preorder(root):
            if root == None:
                return
            res.append(root.val)
            preorder(root.left)
            preorder(root.right)

        preorder(root)

        return res

l = TreeNode(1)
l.right = TreeNode(2)
l.left = None
l.right.left = TreeNode(3)

r = Solution()
res = r.preorderTraversal(l)
print(res)