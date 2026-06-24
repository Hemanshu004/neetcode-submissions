class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        premap={i:[] for i in range(numCourses)}
        for crs,pre in prerequisites:
            premap[crs].append(pre)
        visit=set()

        def dfs(crs):
            if crs in visit:
                return False
            if premap[crs]==[]:
                return True
            
            visit.add(crs)
            for nei in premap[crs]:
                if not dfs(nei):
                    return False
            visit.remove(crs)
            premap[crs]=[]
            return True

        
        for c in range(numCourses):
            if not dfs(c):
                return False
        return True