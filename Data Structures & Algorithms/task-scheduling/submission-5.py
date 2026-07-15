class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        if not tasks:
            return 0
        count=Counter(tasks)
        maxheap=[]
        for char,cnt in count.items():
            maxheap.append(-cnt)
        
        heapq.heapify(maxheap)

        maxcnt=-1*(heapq.heappop(maxheap))
        maxchar=1
        while maxheap:
            cnt=-1*(heapq.heappop(maxheap))
            if cnt==maxcnt:
                maxchar+=1
        
        time=(maxcnt-1)*(n+1)+maxchar
        return max(len(tasks),time)


