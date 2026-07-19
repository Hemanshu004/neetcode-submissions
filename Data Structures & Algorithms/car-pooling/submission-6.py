class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        minheap=[]
        trips.sort(key=lambda t:t[1])
        curpass=0
        for numpass,start,end in trips:
            while minheap and start>=minheap[0][0]:
                prev_end,prev_pass=heapq.heappop(minheap)
                curpass-=prev_pass
            
            curpass+=numpass
            if curpass>capacity:
                return False
            
            heapq.heappush(minheap,[end,numpass])
        return True 

