class Solution:
    def buildMatrix(self, k: int, rowConditions: List[List[int]], colConditions: List[List[int]]) -> List[List[int]]:
        def topsort(edges):
            indegree=[0]*(k+1)
            adj=[[]for _ in range(k+1)]
            for u,v in edges:
                indegree[v]+=1
                adj[u].append(v)
            

            order=[]
            q=deque()
            for i in range(1,k+1):
                if not indegree[i]:
                    q.append(i)
            

            while q:
                node=q.popleft()
                order.append(node)

                for nei in adj[node]:
                    indegree[nei]-=1
                    if indegree[nei]==0:
                        q.append(nei)
            return order

        row_order=topsort(rowConditions)
        if not row_order: return[]
        col_order=topsort(colConditions)
        if not col_order: return[]

        val_to_row={n:i for i,n in enumerate(row_order)}
        val_to_col={n:i for i,n in enumerate(col_order)}

        res=[[0]*k for _ in range(k)]
        for num in range(1,k+1):
            r,c=val_to_row[num],val_to_col[num]
            res[r][c]=num
            
        return res
