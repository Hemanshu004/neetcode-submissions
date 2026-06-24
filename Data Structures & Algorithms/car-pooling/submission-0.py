class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        trips.sort(key=lambda t:t[1])
        heap=[]
        curpass=0
        for t in trips:
            numpass,start,end=t
            while heap and heap[0][0]<=start:
                curpass -=heap[0][1]
                heapq.heappop(heap)
            
            curpass+=numpass
            if curpass>capacity:
                return False
            heapq.heappush(heap,[end,numpass])
        return True