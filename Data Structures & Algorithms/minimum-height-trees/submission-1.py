class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        adj={i:[] for i in range(n)}
        for u,v in edges:
            adj[u].append(v)
            adj[v].append(u)

        def dfs(node,visit,parent):
            h=0
            if node in visit:
                return 
            
            visit.add(node)
            for nei in adj[node]:
                if nei !=parent:
                    h=max(h,dfs(nei,visit,node)+1)
            return h
           

        res=[]
        for i in range(n):
            h=dfs(i,set(),-1)
            res.append(h)
            
        
        min_h=min(res)
        height=[]
        for i,h in enumerate(res):
            if min_h==h:
                height.append(i)
            
        return height


            
        

