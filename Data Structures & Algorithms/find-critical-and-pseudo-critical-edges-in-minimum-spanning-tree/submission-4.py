class Unionfind:
    def __init__(self,n):
        self.parent=list(range(n))
        self.rank=[1]*n
    def find(self,x):
        if self.parent[x]!=x:
            self.parent[x]=self.find(self.parent[x])
        return self.parent[x]
    def union(self,a,b):
        rootA=self.find(a)
        rootB=self.find(b)
        
        if rootA==rootB:
            return False
        
        if self.rank[rootA] > self.rank[rootB]:
            self.parent[rootB] = rootA
            self.rank[rootA] += self.rank[rootB]
        else:
            self.parent[rootA] = rootB
            self.rank[rootB] += self.rank[rootA]

        return True


class Solution:
    def findCriticalAndPseudoCriticalEdges(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        for i,e in enumerate(edges):
            e.append(i)
        
        edges.sort(key=lambda e:e[2])

        mst_weight=0
        uf=Unionfind(n)
        for v1,v2,w,i in edges:
            if uf.union(v1,v2):
                mst_weight+=w
        
        critical,pseudo=[],[]
        for n1, n2, e_weight, i in edges:
            weight=0
            uf=Unionfind(n)
            for v1, v2, w, j in edges:
                if i!=j and uf.union(v1,v2):
                    weight+=w
            
            if max(uf.rank)!=n or weight>mst_weight:
                critical.append(i)
                continue
            
            uf=Unionfind(n)
            uf.union(n1,n2)
            weight=e_weight
            for v1,v2,w,j in edges:
                if uf.union(v1,v2):
                    weight+=w
            
            if weight==mst_weight:
                pseudo.append(i)
        
        return [critical,pseudo]









        