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
# @param t1 TreeNode类
# @param t2 TreeNode类
# @return TreeNode类
#
class Solution:
    def mergeTrees(self , t1 , t2 ):
        # write code here
        if not t1:
            return t2
        if not t2:
            return t1

        new = TreeNode(t1.val+t2.val)
        new.left = self.mergeTrees(t1.left,t2.left)
        new.right = self.mergeTrees(t1.right,t2.right)

        return new

l1 = TreeNode(1)
l1.right = TreeNode(2)
l1.left = TreeNode(3)
l1.left.left = TreeNode(5)

l2 = TreeNode(2)
l2.right = TreeNode(3)
l2.right.right = TreeNode(7)
l2.left = TreeNode(1)
l2.left.right = TreeNode(4)


r = Solution()
res = r.mergeTrees(l1,l2)
print(res.val,res.left.val,res.right.val,res.left.left.val,res.left.right.val,res.right.right.val)