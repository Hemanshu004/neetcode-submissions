class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        maxheap=[-x for x in nums]
        heapq.heapify(maxheap)
        for _ in range(k-1):
            heapq.heappop(maxheap)
        
        return -1*(maxheap[0])