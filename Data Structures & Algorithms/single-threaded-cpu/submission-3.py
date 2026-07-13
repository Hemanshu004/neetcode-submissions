class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        for i,t in enumerate(tasks):
            t.append(i)
        tasks.sort(key=lambda t:t[0])

        res=[]
        minheap=[]
        heapq.heapify(minheap)
        i=0
        time=0
        while i<len(tasks) or minheap:
            while i<len(tasks) and time>=tasks[i][0]:
                heapq.heappush(minheap,[tasks[i][1],tasks[i][2]])
                i+=1
            
            if not minheap:
                time=tasks[i][0]
            else:
                proctime,index=heapq.heappop(minheap)
                res.append(index)
                time+=proctime
        return res

