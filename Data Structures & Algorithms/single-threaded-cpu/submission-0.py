class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        minheap=[]
        minheap2=[]
        res=[]
        time=0
        for i,(x,y) in enumerate (tasks):
            minheap.append([x,y,i])
        heapq.heapify(minheap)

        while minheap or minheap2:
            while minheap and minheap[0][0] <=time:
                x,y,i = heapq.heappop(minheap)

                heapq.heappush(minheap2,[y,i])

            if not minheap2:
                time=minheap[0][0]
                continue


            y,i =heapq.heappop(minheap2)
            time +=y
            res.append(i)
        return res