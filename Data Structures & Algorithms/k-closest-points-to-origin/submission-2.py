class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        minheap=[]
        distance=0
        for x,y in points:
            distance=math.sqrt(((0-x)*(0-x))+((0-y)*(0-y)))
            minheap.append([distance,[x,y]])

        heapq.heapify(minheap)
        res=[]
        for _ in range(k):
            points=heapq.heappop(minheap)[1]
            res.append(points)
        return res 
