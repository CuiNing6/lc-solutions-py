#coding:utf-8
#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
#
# @param num int整型一维数组
# @return int整型二维数组
#
class Solution:
    def permute(self , num ):
        # write code here
        if not num:
            return []

        res = []
        track = []
        visit = [0]*len(num)

        def dfs(num,track,res,visit):
            if len(track) == len(num):
                if track not in res:
                    res.append(track[:])
                return

            for i in range(len(num)):
                if visit[i]:
                    continue
                visit[i] = 1
                track.append(num[i])
                dfs(num,track,res,visit)
                visit[i] = 0
                track.pop()

        dfs(num, track, res,visit)

        return res

    def permute_v1(self , num ):
        # write code here
        if not num:
            return []

        res = []
        track = []
        visit = [0]*len(num)

        def dfs(num,track,res,visit):
            if len(track) == len(num):
                if track not in res:
                    res.append(track[:])
                    res.sort()
                return

            for i in range(len(num)):
                if visit[i]:
                    continue
                if i>0 and num[i] == num[i-1] and not visit[i-1]:
                    continue
                visit[i] = 1
                track.append(num[i])
                dfs(num,track,res,visit)
                visit[i] = 0
                track.pop()

        dfs(num, track, res, visit)

        return res

    def permute_v2(self,num):
        res = []
        track = []
        visit = [0]*len(num)

        def dfs(num,track,visit,start):
            res.append(track[:])

            for i in range(start,len(num)):
                if visit[i]:
                    continue
                visit[i] = 1
                track.append(num[i])
                dfs(num,track,visit,i+1)
                visit[i] = 0
                track.pop()

        dfs(num,track,visit,0)

        return res

    def permute_v3(self,n,k):
        res = []
        track = []

        def dfs(n,k,start,track):
            if k == len(track):
                res.append(track[:])

            for i in range(start,n):
                track.append(i)
                dfs(n,k,i+1,track)
                track.pop()

        dfs(n+1,k,1,track)

        return res

num = [1,2,3]
n = 4
k = 2
r = Solution()
res = r.permute(num)
# res = r.permute_v3(4,2)
print(res)





