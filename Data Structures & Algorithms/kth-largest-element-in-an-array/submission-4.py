class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        Maxheap=[-x for x in nums]
        res=[]
        heapq.heapify(Maxheap)
        for _ in range(k-1):
            n=heapq.heappop(Maxheap)
        
        return -heapq.heappop(Maxheap)