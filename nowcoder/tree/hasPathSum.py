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
# @param sum int整型
# @return bool布尔型
#
class Solution:
    def hasPathSum(self , root , sum ):
        # write code here
        if root == None:
            return False

        if sum == root.val and root.left is None and root.right is None:
            return True

        return self.hasPathSum(root.right, sum-root.val) or self.hasPathSum(root.left, sum-root.val)

l1 = TreeNode(5)
l1.right = TreeNode(8)
l1.left = TreeNode(4)
l1.right.right = TreeNode(9)
l1.right.left = None
l1.left.left = TreeNode(1)
l1.left.right = TreeNode(11)
l1.left.right.left = TreeNode(2)
l1.left.right.right = TreeNode(7)

r = Solution()
res = r.hasPathSum(l1,22)
print(res)


