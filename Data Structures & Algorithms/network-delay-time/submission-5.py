class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj={i:[] for i in range(1,n+1)}
        for u,v,t in times:
            adj[u].append([t,v])
        
        minheap=[[0,k]]
        visit=set()
        time=0
        while minheap:
            t,u=heapq.heappop(minheap)
            if u in visit:
                continue
            time=t
            
            visit.add(u)
            for t2,nei in adj[u]:
                if nei not in visit:
                    heapq.heappush(minheap,[time+t2,nei])
        

        return time if len(visit)==n else -1
                 