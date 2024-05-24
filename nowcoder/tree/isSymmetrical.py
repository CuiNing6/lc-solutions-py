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
    def isSymmetrical(self , pRoot ):
        # write code here
        if not pRoot:
            return True

        res = []

        def levelOrder(pRoot,level):
            if len(res) < level:
                res.append([])

            if not pRoot:
                res[level - 1].append(-1)
                return
            else:
                res[level-1].append(pRoot.val)

            levelOrder(pRoot.left,level+1)
            levelOrder(pRoot.right,level+1)

        levelOrder(pRoot,1)

        for i in res:
            if i != i[::-1]:
                return False

        return True

l1 = TreeNode(1)
l1.right = TreeNode(2)
l1.left = TreeNode(2)
l1.right.left = TreeNode(4)
l1.right.right = TreeNode(3)
l1.left.left = TreeNode(3)
l1.left.right = TreeNode(4)

l2 = TreeNode(1)
l2.right = TreeNode(2)
l2.left = TreeNode(2)
l2.right.left = None
l2.right.right = TreeNode(3)
l2.left.left = None
l2.left.right = TreeNode(3)

r = Solution()
res = r.isSymmetrical(l1)
print (res)