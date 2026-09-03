class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        adj=defaultdict(list)
        for i in range(len(points)):
            x,y=points[i]
            for j in range(i+1,len(points)):
                x2,y2=points[j]
                dist=abs(x-x2)+abs(y-y2)
                adj[i].append([dist,j])
                adj[j].append([dist,i])
        

        minheap=[(0,0)]
        res=0
        visit=set()
        while minheap:
            cost,node=heapq.heappop(minheap)
            if node in visit:
                continue
            if len(visit)==len(points):
                break
            res+=cost
            visit.add(node)
            
            for neicost,nei in adj[node]:
                if nei not in visit:
                    heapq.heappush(minheap,[neicost,nei])
        
        

        return res



            
