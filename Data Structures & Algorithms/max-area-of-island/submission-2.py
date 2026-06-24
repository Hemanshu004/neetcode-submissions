class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows,cols=len(grid),len(grid[0])
        visit=set()
        def dfs(r,c):
            if r<0 or c<0 or r>=rows or c>=cols or grid[r][c]==0 or (r,c) in visit:
                return 0
            
            visit.add((r,c))
            area=1
            area+=dfs(r+1,c)
            area+=dfs(r,c+1)
            area+=dfs(r-1,c)
            area+=dfs(r,c-1)
            return area

        area=0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c]==1 and (r,c) not in visit:
                    curr=dfs(r,c)
                    area=max(area,curr)
        return area