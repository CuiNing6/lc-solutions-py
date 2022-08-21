class Solution:
    def solve(self, grid):
        # write code here
        if grid is None:
            return None

        res = 0

        def research(i, j):
            if j >= len(grid[0]) or i >= len(grid) or j < 0 or grid[i][j] == 0:
                return

            grid[i][j] = 0

            if i == 0:
                research(i, j - 1)
                research(i, j - 1)
                research(i, j + 1)
            elif j == 0:
                research(i - 1, j)
                research(i + 1, j)
                research(i, j + 1)
            else:
                research(i - 1, j)
                research(i, j - 1)
                research(i + 1, j)
                research(i, j + 1)

        for i, row in enumerate(grid):
            for j, col in enumerate(row):
                if col == 1:
                    research(i, j)
                    res = res + 1

        return res


prices = [[1,1,1,1,1,1,1,1,1,1],[1,1,1,1,1,1,1,1,1,1],[1,1,1,1,1,1,1,1,1,1],[1,1,1,1,1,1,1,1,1,1],[1,1,1,1,1,1,1,1,1,1],[1,1,1,1,1,1,1,1,1,1],[1,1,1,1,1,1,1,1,1,1],[1,1,1,1,1,1,1,1,1,1],[1,1,1,1,1,1,1,1,1,1],[1,1,1,1,1,1,1,1,1,1]]
prices1 = [[1]]
run = Solution()
res =  run.solve(prices1)
print (res)