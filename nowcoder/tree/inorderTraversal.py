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
    def inorderTraversal(self , root ):
        # write code here
        res = []

        def inorder(root):
            if root == None:
                return

            inorder(root.left)
            res.append(root.val)
            inorder(root.right)

        inorder(root)

        return res

l = TreeNode(1)
l.left = TreeNode(2)
l.right = None
l.left.right = TreeNode(3)

l1 = None

l2 = TreeNode(1)
l2.left = TreeNode(2)

r = Solution()
res = r.inorderTraversal(l2)
print(res)