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
    def postorderTraversal(self , root ):
        # write code here
        res = []
        def postorder(root):
            if root == None:
                return

            postorder(root.left)
            postorder(root.right)

            res.append(root.val)

        postorder(root)

        return res

l = TreeNode(1)
l.right = TreeNode(2)
l.left = None
l.right.left = TreeNode(3)

r = Solution()
res = r.postorderTraversal(l)
print(res)