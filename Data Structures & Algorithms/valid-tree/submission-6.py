class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        graph={i:[] for i in range(n)}
        for x,y in edges:
            graph[y].append(x)
            graph[x].append(y)

        visit=set()

        def dfs(node,parent):
            if node in visit:
                return False
            
            visit.add(node)

            for nei in graph[node]:
                if nei==parent:
                    continue
                if not dfs(nei,node):
                    return False
        
            return True
        
        if dfs(0,-1) and len(visit)==n:
            return True
        return False
        


        