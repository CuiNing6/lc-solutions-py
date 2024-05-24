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
# @param pRoot TreeNode类
# @return TreeNode类
#
class Solution:
    def Mirror(self , pRoot ):
        # write code here
        if not pRoot:
            return None

        value = pRoot.left
        pRoot.left = pRoot.right
        pRoot.right = value

        self.Mirror(pRoot.left)
        self.Mirror(pRoot.right)

        return pRoot

l1 = TreeNode(8)
l1.right = TreeNode(10)
l1.left = TreeNode(6)
l1.right.left = TreeNode(9)
l1.right.right = TreeNode(11)
l1.left.left = TreeNode(5)
l1.left.right = TreeNode(7)


r = Solution()
res = r.Mirror(l1)
print(res.val,res.left.val,res.right.val,res.left.left.val,res.left.right.val,res.right.left.val,res.right.right.val)