class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n==1:
            return [0]
        
        adj={i:[]for i in range(n)}
        for u,v in edges:
            adj[u].append(v)
            adj[v].append(u)
        
        edge_cnt={}
        leaves=deque()
        for src,nei in adj.items():
            edge_cnt[src]=len(nei)
            if len(nei)==1:
                leaves.append(src)
            

        while leaves:
            if n<=2:
                return list(leaves)
            for i in range(len(leaves)):
                node=leaves.popleft()
                n-=1
                for nei in adj[node]:
                    edge_cnt[nei]-=1
                    if edge_cnt[nei]==1:
                        leaves.append(nei)
