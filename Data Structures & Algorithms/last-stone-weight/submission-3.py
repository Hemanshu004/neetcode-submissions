class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        max_heap=[-s for s in stones]
        heapq.heapify(max_heap)
        while len(max_heap)>1:
            res=heapq.heappop(max_heap)-heapq.heappop(max_heap)
            heapq.heappush(max_heap,res)
        
        if not max_heap:
            return 0
        return -1*(max_heap[0])
    




