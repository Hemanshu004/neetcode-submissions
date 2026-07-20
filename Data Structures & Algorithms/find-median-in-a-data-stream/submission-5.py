class MedianFinder:

    def __init__(self):
        self.maxheap=[] #small
        self.minheap=[] #large

    def addNum(self, num: int) -> None:
        heapq.heappush(self.maxheap,-1*num)

        if self.maxheap and self.minheap and (-1*self.maxheap[0])>self.minheap[0]:
            val=-1*heapq.heappop(self.maxheap)
            heapq.heappush(self.minheap,val)
        
        if len(self.maxheap)>len(self.minheap)+1:
            val=-1*heapq.heappop(self.maxheap)
            heapq.heappush(self.minheap,val)

        if len(self.minheap)>len(self.maxheap)+1:
            val=heapq.heappop(self.minheap)
            heapq.heappush(self.maxheap,-1*val)

                          

    def findMedian(self) -> float:
        if len(self.maxheap)>len(self.minheap):
            return -1*(self.maxheap[0])

        if len(self.maxheap)<len(self.minheap):   
            return self.minheap[0]
        
        return ((-1*self.maxheap[0])+self.minheap[0])/2

            
        
        
        
        