class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        adj=defaultdict(list)
        for prereq,crs in prerequisites:
            adj[crs].append(prereq)
        
        def dfs(crs):
            if crs not in premap:
                premap[crs]=set()
                for prereq in adj[crs]:
                    premap[crs].update(dfs(prereq))
                premap[crs].add(crs)
            return premap[crs]

  
        premap={}
        for crs in range(numCourses):
            dfs(crs)
        

        res=[]
        for u,v in queries:
            res.append(u in premap[v])
        return res