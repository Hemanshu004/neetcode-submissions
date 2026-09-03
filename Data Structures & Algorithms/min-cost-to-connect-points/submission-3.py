class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n,node=len(points),0
        dist = [100000000] * n
        res,edges=0,0
        visit=[False]*n


        while edges<n-1:
            visit[node]=True
            nextnode=-1
            for i in range(n):
                if visit[i]:
                    continue
                
                curr_dist=abs(points[i][0]-points[node][0])+abs(points[i][1]-points[node][1])

                dist[i]=min(dist[i],curr_dist)
                if nextnode==-1 or dist[i]<dist[nextnode]:
                    nextnode=i
            
            res+=dist[nextnode]
            edges+=1
            node=nextnode
        return res
