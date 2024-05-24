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
# @return int整型
#
class Solution:
    def maxDepth(self , root ):
        # write code here
        if root == None:
            return 0

        r = self.maxDepth(root.right)
        l = self.maxDepth(root.left)

        return max(l,r) + 1


l1 = TreeNode(1)
l1.right = TreeNode(3)
l1.left = TreeNode(2)
l1.right.left = TreeNode(4)
l1.right.right = None
l1.left.left = TreeNode(5)


r = Solution()
res = r.maxDepth(l1)
print(res)
