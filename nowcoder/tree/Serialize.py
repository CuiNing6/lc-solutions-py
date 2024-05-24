# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    def Serialize(self, root):
        # write code here
        if not root:
            return []

        res = []

        def preorder(root):
            if not root:
                res.append("#")
                return

            res.append(root.val)

            preorder(root.left)
            preorder(root.right)

        preorder(root)

        return ','.join(str(x) for x in res)


    def Deserialize(self, s):
        # write code here
        if not s:
            return None

        self.s = s.split(',')
        self.index = 0

        root = self.preorder(s.split(','))

        return root

    def preorder(self, s):
        if s[0] == '#':
            self.index += 1
            return None

        root = TreeNode(int(s[0]))
        self.index += 1
        if len(s) == 1:
            return root
        root.left = self.preorder(s[1:])
        if self.index < len(self.s):
            root.right = self.preorder(self.s[self.index:])

        return root




l1 = TreeNode(1)
l1.right = TreeNode(3)
l1.left = TreeNode(2)
l1.right.left = TreeNode(6)
l1.right.right = TreeNode(7)


r = Solution()
res = r.Serialize(l1)
print(res)
res_d = r.Deserialize(res)
print(res_d.val,res_d.right.val,res_d.right.left.val,res_d.right.right.val,res_d.left.val)