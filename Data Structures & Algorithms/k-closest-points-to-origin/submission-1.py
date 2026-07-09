import math 
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        min_heap=[]
        closest=[]
        for x,y in points:
            res=(x*x)+(y*y)
            min_heap.append((res,x,y))
        
        i=0
        heapq.heapify(min_heap)
        while i!=k:
            distance=heapq.heappop(min_heap)
            x=distance[1]
            y=distance[2]
            closest.append([x,y])
            i+=1
        return closest
            
