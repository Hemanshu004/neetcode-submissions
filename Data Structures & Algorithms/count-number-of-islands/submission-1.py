class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visit=set()
        row,cols=len(grid),len(grid[0])
        def dfs(i,j):
            if i<0 or j<0 or  i>=row or j>=cols or grid[i][j]=="0" or (i,j) in visit:
                return 

            visit.add((i,j))
            dfs(i,j+1)
            dfs(i+1,j)
            dfs(i-1,j)
            dfs(i,j-1)


        islands=0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]=="1" and (i,j)not in visit:
                    dfs(i,j)
                    islands+=1
        return islands