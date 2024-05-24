# 给你一个整数数组 nums，有一个大小为 k 的滑动窗口从数组的最左侧移动到数组的最右侧。你只可以看到在滑动窗口内的 k 个数字。滑动窗口每次只向右移动一位。
# 返回滑动窗口中的最大值 。
#
# 输入：nums = [1,3,-1,-3,5,3,6,7], k = 3
# 输出：[3,3,5,5,6,7]
# 解释：
# 滑动窗口的位置                最大值
# ---------------               -----
# [1  3  -1] -3  5  3  6  7       3
#  1 [3  -1  -3] 5  3  6  7       3
#  1  3 [-1  -3  5] 3  6  7       5
#  1  3  -1 [-3  5  3] 6  7       5
#  1  3  -1  -3 [5  3  6] 7       6
#  1  3  -1  -3  5 [3  6  7]      7


import collections
def maxSlidingWindow(nums, k):
    n = len(nums)
    Q = collections.deque()

    res = []

    for i in range(n):
        while len(Q) > 0 and nums[i] >= nums[Q[-1]]:
            Q.pop()
        Q.append(i)

        if i - Q[0] + 1 > k:
            Q.popleft()

        if i >= k-1:
            res.append(nums[Q[0]])

    return res

nums = [1,3,-2,-3,-1,5,3,6,7]
k = 3

res = maxSlidingWindow(nums, k)
print(res)
