class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        directions=[[1,0],[0,1],[-1,0],[0,-1]]
        rows=len(grid)
        cols=len(grid[0])
        fresh=0
        q=deque()
        time=0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c]==1:
                    fresh+=1
                if grid[r][c]==2:
                    q.append([r,c])
            
        while fresh>0 and q:
            for _ in range(len(q)):
                r,c=q.popleft()
                for dr,dc in directions:
                    nr,nc=r+dr,c+dc

                    if (nr<0 or nc<0 or nr>=rows or nc>=cols or grid[nr][nc]==0 or grid[nr][nc]==2):
                        continue
                        
                    grid[nr][nc]=2
                    q.append([nr,nc])
                    fresh-=1
            time+=1
        
        return time if fresh==0 else -1
