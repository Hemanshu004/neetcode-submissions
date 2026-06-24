class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows,cols=len(grid),len(grid[0])
        visit=set()
        def dfs(r,c):
            if r<0 or c<0 or r>=rows or c>=cols or grid[r][c]=="0":
                return 
                
            if (r,c) in visit:
                return 
                    
            visit.add((r,c))
            dfs(r+1,c)
            dfs(r,c+1)
            dfs(r-1,c)
            dfs(r,c-1)
                    
        island=0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if (r,c) not in visit and grid[r][c]=="1":
                    island+=1
                    dfs(r,c)
        return island

            
        

                