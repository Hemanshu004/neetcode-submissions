class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj={i:[]for i in range(1,n+1)}
        for u,v,t in times:
            adj[u].append([t,v])
        
        minheap=[[0,k]]
        visit=set()
        while minheap:
            count,node=heapq.heappop(minheap)
            if node in visit:
                continue
            visit.add(node)
            if len(visit)==n:
                return count
      
            for neicost,nei in adj[node]:
                if nei not in visit: 
                    heapq.heappush(minheap,[count+neicost,nei])


        return -1
        