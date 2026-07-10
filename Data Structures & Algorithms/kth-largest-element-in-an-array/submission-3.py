class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        Maxheap=[-x for x in nums]
        res=[]
        heapq.heapify(Maxheap)
        while k>0:
            n=heapq.heappop(Maxheap)
            res.append(n*-1)
            k-=1
        
        return res[-1]