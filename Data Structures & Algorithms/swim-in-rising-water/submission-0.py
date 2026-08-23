class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        directions=[[-1,0],[1,0],[0,-1],[0,1]]
        visit=set()
        minheap=[[grid[0][0],0,0]]
        next_node=float("inf")
        while minheap:
            t,r,c=heapq.heappop(minheap)
            if (r,c) in visit:
                continue
            
            if r==len(grid)-1 and c==len(grid[0])-1:
                return t
            
            visit.add((r,c))
            for dr,dc in directions:
                nr,nc=r+dr,c+dc
                if nr<0 or nc<0 or nr>=len(grid) or nc>=len(grid[0]) or (nr,nc) in visit:
                    continue
                
                new_t=max(t,grid[nr][nc])
                
                heapq.heappush(minheap,[new_t,nr,nc])
            
        
            

            

















        return max(res)