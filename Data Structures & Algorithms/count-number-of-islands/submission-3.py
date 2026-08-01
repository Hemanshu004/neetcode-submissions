class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visit=set()
        rows=len(grid)
        cols=len(grid[0])
        def dfs(r,c):
            if r<0 or c<0 or r>=rows or c>=cols or grid[r][c]=="0" or (r,c) in visit:
                return 
            
            visit.add((r,c))

            dfs(r+1,c)
            dfs(r,c+1)
            dfs(r-1,c)
            dfs(r,c-1)
            return 

        island=0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c]=="1" and (r,c) not in visit:
                    island+=1
                    dfs(r,c)
        return island
