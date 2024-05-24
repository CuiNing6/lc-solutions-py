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
# @return int整型二维数组
#
class Solution:
    def levelOrder(self , root ):
        # write code here
        res = []

        def level(root, le):
            if root == None:
                return

            if len(res) < le:
                res.append([])

            res[le-1].append(root.val)
            level(root.left, le+1)
            level(root.right, le+1)

        level(root, 1)

        return res

l = TreeNode(3)
l.right = TreeNode(20)
l.left = TreeNode(9)
l.left.left = TreeNode(15)
l.left.right = TreeNode(7)

r = Solution()
res = r.levelOrder(l)
print(res)