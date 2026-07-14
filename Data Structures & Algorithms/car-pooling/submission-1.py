class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        trips.sort(key=lambda t:t[1])

        minheap=[]
        curpass=0
        
        for numpass,start,end in trips:
            while minheap and minheap[0][0]<=start:
                curpass-=heapq.heappop(minheap)[1]
            

            curpass+=numpass
            if curpass>capacity:
                return False
            

            heapq.heappush(minheap,[end,numpass])
        return True
