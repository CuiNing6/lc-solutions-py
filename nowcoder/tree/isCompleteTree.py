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
    def isCompleteTree(self , root ):
        # write code here
        if root == None:
            return True

        s = [(root,1)]
        i = 0

        while s:
            i += 1
            node, v = s.pop(0)
            if i != v:
                return False

            if node.left:
                s.append((node.left,v*2))
            if node.right:
                s.append((node.right,v*2+1))

        return True

l1 = TreeNode(1)
l1.right = TreeNode(3)
l1.left = TreeNode(2)
l1.left.left = TreeNode(4)
l1.left.right = TreeNode(5)
l1.right.right = TreeNode(6)


r = Solution()
res = r.isCompleteTree(l1)
print(res)