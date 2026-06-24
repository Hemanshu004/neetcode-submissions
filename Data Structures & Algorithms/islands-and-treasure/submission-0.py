class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        if not grid:
            return 
        visit=set()
        q=deque()

        def calD(r,c):
            if r>=len(grid) or c>=len(grid[0])or r<0 or c<0 or grid[r][c]==-1 or (r,c) in visit:
                return     
            visit.add((r,c))
            q.append((r,c))       

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c]==0:
                    visit.add((r,c))
                    q.append((r,c))
        
        dist=0
        while q:
            for i in range(len(q)):
                r,c=q.popleft()
                grid[r][c]=dist
                calD(r+1,c)
                calD(r,c+1)
                calD(r-1,c)
                calD(r,c-1)
            dist+=1