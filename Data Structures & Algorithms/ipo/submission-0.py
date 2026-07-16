class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        minheap=[[capital[i],profits[i]] for i in range(len(profits))]
        maxheap=[]
        heapq.heapify(minheap)
        
        for i in range(k):
            while minheap and minheap[0][0]<=w:
                cap,p=heapq.heappop(minheap)
                heapq.heappush(maxheap,-p)
            
            if not maxheap:
                break
            w+=-1*(heapq.heappop(maxheap))
        return w