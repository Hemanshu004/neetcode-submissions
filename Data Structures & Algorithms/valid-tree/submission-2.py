class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        num={i:[] for i in range(n)}
        for crs ,dst in edges:
            num[crs].append(dst)
            num[dst].append(crs)
        

        visit=set()
        def dfs(node,parent):
            if node in visit:
                return False
            visit.add(node)
            for nei in num[node]:
                if nei==parent:
                    continue
                if not dfs(nei,node):
                    return False
            return True
        
        return dfs(0,-1) and len(visit)==n
            

