class Interval:
    def __init__(self, a=0, b=0):
        self.start = a
        self.end = b

#
class Solution:
    def merge(self , intervals ):
        # write code here
        if intervals is None:
            return None

        intervals = sorted(intervals,key=lambda x: x.start)
        res = []

        i, n = 0, len(intervals)

        while i < n:
            l = intervals[i].start
            r = intervals[i].end

            while i < n-1 and r >= intervals[i+1].start:
                r = max(r, intervals[i+1].end)
                i = i + 1

            res.append(Interval(l, r))
            i = i + 1

        return res

intervals = []
intervals.append(Interval(10,30))
intervals.append(Interval(20,60))
intervals.append(Interval(80,100))
intervals.append(Interval(150,180))

run = Solution()
res =  run.merge(intervals)
print (res[0].start,res[1].start,res[2].start)
print (res[0].end,res[1].end,res[2].end)