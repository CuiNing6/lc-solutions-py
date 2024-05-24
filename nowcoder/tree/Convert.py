# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    def Convert(self, pRootOfTree):
        # write code here
        if pRootOfTree is None:
            return None

        res = []

        def inorder(pRootOfTree):
            if not pRootOfTree:
                return None

            inorder(pRootOfTree.left)
            res.append(pRootOfTree)
            inorder(pRootOfTree.right)

        inorder(pRootOfTree)

        for i,v in enumerate(res[0:len(res)-1]):
            v.right = res[i+1]
            res[i+1].left = v

        return res[0]

l2 = TreeNode(10)
l2.right = TreeNode(14)
l2.left = TreeNode(6)
l2.right.left = TreeNode(12)
l2.right.right = TreeNode(16)
l2.left.left = TreeNode(4)
l2.left.right = TreeNode(8)



r = Solution()
res = r.Convert(l2)
print(res.val,res.right.val,res.right.right.val,res.right.right.right.val,res.right.right.right.right.val,res.right.right.right.right.right.val,res.right.right.right.right.right.right.val)