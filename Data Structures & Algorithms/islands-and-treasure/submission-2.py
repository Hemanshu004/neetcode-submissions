class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        row,cols=len(grid),len(grid[0])
        visit=set()
        q=deque()

        def add(r,c):
            if r<0 or c<0 or r>=row or c>=cols or grid[r][c]==-1 or (r,c) in visit:
                return 

            q.append([r,c])
            visit.add((r,c))        
        

        for r in range(row):
            for c in range(cols):
                if grid[r][c]==0:
                    q.append([r,c])
                    visit.add((r,c))
        dist=0
        while q:
            for i in range(len(q)):
                r,c=q.popleft()
                grid[r][c]=dist
                add(r+1,c)
                add(r,c+1)
                add(r-1,c)
                add(r,c-1)
            dist+=1