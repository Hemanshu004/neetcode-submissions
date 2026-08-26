class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        adj=defaultdict(list)
        INF = float("inf")
        dist=[[INF]*(k+2) for _ in range(n)]
        for x,y,cst in flights:
            adj[x].append([y,cst])
        
        dist[src][0]=0
        minheap=[(0,src,-1)]
        while minheap:
            cst,node,stops=heapq.heappop(minheap)

            if dst==node:
                return cst
            
            if stops==k or dist[node][stops+1]<cst:
                continue
            
            for nei,w in adj[node]:
                nextcst=cst+w
                nextstop=stops+1
                if dist[nei][nextstop+1]>nextcst:
                    dist[nei][nextstop+1]=nextcst
                    heapq.heappush(minheap,(nextcst,nei,nextstop))
            
        
        return -1
                
            
                    
