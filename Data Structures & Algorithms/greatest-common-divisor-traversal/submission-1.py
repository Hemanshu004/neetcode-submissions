class unionfind:
    def __init__(self,n):
        self.parent=[i for i in range(n)]
        self.rank=[1]*n
        self.count=n
    
    def find(self,x):
        if self.parent[x]!=x:
            self.parent[x]=self.find(self.parent[x])
        
        return self.parent[x]
    
    def union(self,a,b):
        rootA=self.find(a)
        rootB=self.find(b)

        if rootA==rootB:
            return False
        
        if self.rank[rootA]<self.rank[rootB]:
            self.parent[rootA]=rootB
            self.rank[rootB]+=self.rank[rootA]
        else:
            self.parent[rootB]=rootA
            self.rank[rootA]+=self.rank[rootB]
        self.count-=1
        


class Solution:
    def canTraverseAllPairs(self, nums: List[int]) -> bool:
        uf=unionfind(len(nums))
        factor_index={}
        for i ,n in enumerate(nums):
            f=2
            while f*f<=n:
                if n%f==0:
                    if f in factor_index:
                        uf.union(i,factor_index[f])
                    else:
                        factor_index[f]=i

                    while n%f==0:
                        n=n//f
                f+=1
            
            if n>1:
                if n in factor_index:
                    uf.union(i,factor_index[n])
                else:
                    factor_index[n]=i
            
        return uf.count==1


