class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        maxheap=[(c,p) for p,c in zip(profits,capital)]
        heapq.heapify(maxheap)
        minheap=[]
        for _ in range(k):
            while maxheap and maxheap[0][0]<=w:
                c,p=heapq.heappop(maxheap)
                heapq.heappush(minheap,-p)
            
            if not minheap:
                break
            
            w+=-(heapq.heappop(minheap))
        
        return w

            
