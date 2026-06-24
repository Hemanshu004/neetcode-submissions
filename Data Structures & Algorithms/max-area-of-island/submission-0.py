class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        visit=set()
        row,cols=len(grid),len(grid[0])
        def dfs(i,j):
            if i>=row or j>=cols or i<0 or j<0 or grid[i][j]==0 or (i,j) in visit:
                return 0
            visit.add((i,j))
            peri=1
            peri += dfs(i,j+1)
            peri +=dfs(i+1,j)
            peri +=dfs(i,j-1)
            peri +=dfs(i-1,j)
            return peri
        max_peri=0
        for i in range(row):
            for j in range(cols):
                if (i,j) not in visit and grid[i][j]==1:
                    max_peri=max(dfs(i,j),max_peri)
        return max_peri
