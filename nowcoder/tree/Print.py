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
# @return int整型二维数组
#
class Solution:
    def Print(self , pRoot ):
        # write code here
        res = []

        def level(pRoot, le):
            if pRoot == None:
                return

            if len(res) < le:
                res.append([])

            res[le - 1].append(pRoot.val)
            level(pRoot.left, le + 1)
            level(pRoot.right, le + 1)


        level(pRoot, 1)

        for i in range(1, len(res), 2):
            res[i] = res[i][::-1]

        return res

l = TreeNode(1)
l.right = TreeNode(3)
l.left = TreeNode(2)
l.right.left = TreeNode(4)
l.right.right = TreeNode(5)


#{8,6,10,5,7,9,11}
l1 = TreeNode(8)
l1.right = TreeNode(10)
l1.left = TreeNode(6)
l1.right.left = TreeNode(9)
l1.right.right = TreeNode(11)
l1.left.left = TreeNode(5)
l1.left.right = TreeNode(7)


r = Solution()
res = r.Print(l1)
print(res)