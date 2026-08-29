class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        m=numCourses
        indegree=[0]*m
        adj=[[]for _ in range(m)]
        for u,v in prerequisites:
            indegree[v]+=1
            adj[u].append(v)
        
        q=deque()
        for n in range(m):
            if indegree[n]==0:
                q.append(n)
        res=[]
        while q:
            node=q.popleft()
            res.append(node)
            for nei in adj[node]:
                indegree[nei]-=1
                if indegree[nei]==0:
                    q.append(nei)

        if len(res)!=m:
            return []
        return res[::-1]


