class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        adj=defaultdict(list)
        for i,eq in enumerate(equations):
            a,b=eq
            adj[a].append((b,values[i]))
            adj[b].append((a,1/values[i]))
        

        def dfs(src,target,visit):
            if src not in adj or target not in adj:
                return -1
            
            if src==target:
                return 1
            visit.add(src)
            
            for nei,weight in adj[src]:
                if nei not in visit:
                    result=dfs(nei,target,visit)

                    if result!=-1:
                        return weight*result
            return -1


        
        return [dfs(q[0],q[1],set()) for q in queries]