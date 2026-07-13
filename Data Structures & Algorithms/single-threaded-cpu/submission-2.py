class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        for i,t in enumerate(tasks):
            t.append(i)
        tasks.sort(key=lambda t:t[0])

        time=tasks[0][0]
        res=[]
        i=0
        minheap=[]
        heapq.heapify(minheap)
        while i <len(tasks) or  minheap:
            while i<len(tasks) and tasks[i][0]<=time:
                heapq.heappush(minheap,[tasks[i][1],tasks[i][2]])
                i+=1
            if not minheap:
                time=tasks[i][0]
            else:
                proctime,index=heapq.heappop(minheap)
                time+=proctime
                res.append(index)
        return res



        


