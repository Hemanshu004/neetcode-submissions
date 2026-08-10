class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj={i:[]for i in range(n)}
        for x,y in edges:
            adj[x].append(y)
            adj[y].append(x)

        visit=set()
        def bfs(node):
            q=deque([node])
            visit.add(node)
            while q:
                cur=q.popleft()
                for nei in adj[cur]:
                    if nei not in visit:
                        visit.add(nei)
                        q.append(nei)
            
        

        count=0
        for i in range(n):
            if i not in visit:
                bfs(i)
                count+=1
        return count 