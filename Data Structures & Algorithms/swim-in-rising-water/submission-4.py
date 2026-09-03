class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        rows=len(grid)
        cols=len(grid[0])
        directions=[[1,0],[0,1],[-1,0],[0,-1]]
    
        visit=set()
        minheap=[[grid[0][0],0,0]]
        while minheap:
            res,r,c=heapq.heappop(minheap)

            if (r,c) in visit:
                continue
            if r==rows-1 and c==cols-1:
                return res

            visit.add((r,c))
            for dr,dc in directions:
                nr,nc=r+dr,c+dc
                if nr<0 or nc<0 or nr>=rows or nc>=cols or (nr,nc) in visit:
                    continue
                
                new_res=max(res,grid[nr][nc])
                heapq.heappush(minheap,[new_res,nr,nc])
