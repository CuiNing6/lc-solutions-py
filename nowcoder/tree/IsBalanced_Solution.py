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
# @return bool布尔型
#
class Solution:
    def IsBalanced_Solution(self , pRoot ):
        # write code here
        if not pRoot:
            return True

        def deep(pRoot):
            if not pRoot:
                return 0

            l = deep(pRoot.left)
            r = deep(pRoot.right)

            return max(l,r) + 1

        L = deep(pRoot.left)
        R = deep(pRoot.right)

        if abs(L-R) > 1:
            return False
        else:
            return self.IsBalanced_Solution(pRoot.left) and self.IsBalanced_Solution(pRoot.right)


l1 = TreeNode(1)
l1.right = TreeNode(3)
l1.left = TreeNode(2)
l1.left.left = TreeNode(4)
l1.left.right = TreeNode(5)
l1.right.left = TreeNode(6)
l1.right.right = TreeNode(7)


r = Solution()
res = r.IsBalanced_Solution(l1)
print(res)