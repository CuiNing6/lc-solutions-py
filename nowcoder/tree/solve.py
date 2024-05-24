#coding:utf-8
#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
# 求二叉树的右视图
# @param preOrder int整型一维数组 先序遍历
# @param inOrder int整型一维数组 中序遍历
# @return int整型一维数组
#
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    def solve(self , preOrder , inOrder ):
        # write code here
        if not preOrder and not inOrder:
            return None

        root = self.get_root(preOrder,inOrder)

        return self.get_res(root)


    def get_root(self, preOrder, inOrder):
        if not preOrder and not inOrder:
            return None

        root = TreeNode(preOrder[0])

        if set(preOrder) != set(inOrder):
            return None

        index = inOrder.index(preOrder[0])

        root.left = self.get_root(preOrder[1:index+1], inOrder[:index])
        root.right = self.get_root(preOrder[index+1:], inOrder[index+1:])

        return root

    def get_res(self,root):
        if not root:
            return []

        res = []

        def result(root,level):
            if not root:
                return

            if level > len(res):
                res.append([])

            res[level-1].append(root.val)

            result(root.left, level+1)
            result(root.right, level+1)

        result(root,1)

        res_f = []
        for i in res:
            res_f.append(i[-1])

        return res_f

pre = [1, 2, 4, 5, 3]
tin = [4, 2, 5, 1, 3]

r = Solution()
res = r.solve(pre, tin)
print(res)