class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        INF=float("inf")
        prices=[INF]*n
        prices[src]=0
        adj=[[]for _ in range(n)]
        for x,y,cst in flights:
            adj[x].append([y,cst])
        

        q =deque([(0, src, 0)])

        while q:
            cst,node,stops=q.popleft()
            
            if stops>k:
                continue
            
            for nei, neicost in adj[node]:
                new_cst=cst+neicost
                if new_cst<prices[nei]:
                    prices[nei]=new_cst
                    q.append((new_cst,nei,stops+1))
        
        return prices[dst] if prices[dst]!=float("inf") else -1