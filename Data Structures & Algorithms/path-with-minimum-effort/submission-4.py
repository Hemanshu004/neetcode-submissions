class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        directions=[[0,1],[1,0],[-1,0],[0,-1]]
        rows=len(heights)
        cols=len(heights[0])

        minheap=[(0,0,0)]
        visit=set()
        while minheap:
            diff,r,c=heapq.heappop(minheap)
            if r==rows-1 and c==cols-1:
                return diff 
            
            if (r,c) in visit:
                continue

            visit.add((r,c))
            for dr,dc in directions:
                nr,nc=r+dr,c+dc
                if nr<0 or nc<0 or nr>=rows or nc>=cols or (nr,nc) in visit:
                    continue   

                curr_diff=abs(heights[r][c]-heights[nr][nc])
                ans=max(diff,curr_diff)
                heapq.heappush(minheap,(ans,nr,nc))  
        return ans        
