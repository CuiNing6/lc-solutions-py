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
# @param p int整型
# @param q int整型
# @return int整型
#
class Solution:
    def lowestCommonAncestor(self , root , p , q ):
        # write code here
        if not root:
            return -1

        p, q = min(p,q), max(p,q)

        if root.val == p or root.val == q:
            return root.val

        if root.val > p and root.val < q:
            return root.val

        if root.val > q:
            return self.lowestCommonAncestor(root.left, p, q)
        if root.val < p:
            return self.lowestCommonAncestor(root.right, p, q)

        return -1


    def lowestCommonAncestor_v1(self , root , p , q ):
        # write code here
        if not root:
            return -1

        if root.val == p or root.val == q:
            return root.val

        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)

        if left == -1:
            return right
        if right == -1:
            return left
        return root.val





l1 = TreeNode(7)
l1.right = TreeNode(12)
l1.left = TreeNode(1)
l1.right.left = TreeNode(11)
l1.right.right = TreeNode(14)
l1.left.left = TreeNode(0)
l1.left.right = TreeNode(4)
l1.left.right.left = TreeNode(3)
l1.left.right.right = TreeNode(5)


l2 = TreeNode(3)
l2.right = TreeNode(1)
l2.left = TreeNode(5)
l2.right.left = TreeNode(0)
l2.right.right = TreeNode(8)
l2.left.left = TreeNode(6)
l2.left.right = TreeNode(2)
l2.left.right.left = TreeNode(7)
l2.left.right.right = TreeNode(4)



r = Solution()
# res = r.lowestCommonAncestor(l1,12,11)
# print(res)
res = r.lowestCommonAncestor_v1(l2,5,1)
print(res)