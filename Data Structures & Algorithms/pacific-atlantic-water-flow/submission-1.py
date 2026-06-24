class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        row,cols=len(heights),len(heights[0])
        pac, atl = set(), set()
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        def bfs(source,ocean):
            q=deque(source)
            while q:
                r,c=q.popleft()
                if (r,c) in ocean:
                    continue 
                ocean.add((r,c))
                for dr,dc in directions:
                    nr,nc=r+dr,c+dc
                    if(0<=nr<row and 0<=nc<cols and(nr,nc) not in ocean and heights[nr][nc]>=heights[r][c] ):
                        q.append((nr,nc))

                
        


        pacific=[]
        atlantic=[]
        for c in range(cols):
            pacific.append((0,c))
            atlantic.append((row-1,c))
        
        for r in range(row):
            pacific.append((r,0))
            atlantic.append((r,cols-1))
        
        bfs(pacific,pac)
        bfs(atlantic,atl)
        res=[]
        for r in range(row):
            for c in range(cols):
                if (r,c) in pac and (r,c) in atl:
                    res.append((r,c))
        return res