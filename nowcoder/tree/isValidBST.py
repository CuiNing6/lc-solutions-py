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
# @return bool布尔型
#
class Solution:
    def isValidBST(self , root ):
        # write code here
        def preorder(root, left, right):
            if root == None:
                return True

            if left.val > root.val or right.val < root.val:
                return False

            return preorder(root.right,root, right) and preorder(root.left, left, root)

        return preorder(root, TreeNode(float("-inf")), TreeNode(float("inf")))

l1 = TreeNode(1)
l1.right = TreeNode(3)
l1.left = TreeNode(2)


r = Solution()
res = r.isValidBST(l1)
print(res)