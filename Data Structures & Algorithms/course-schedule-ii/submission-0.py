class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        premap={i:[] for i in range(numCourses)}
        for crs,pre in prerequisites:
            premap[crs].append(pre)
        visit=set()
        visiting=set()
        res=[]
        def dfs(crs):
            if crs in visit:
                return True
            
            if crs in visiting:
                return False
            
            visiting.add(crs)

            for pre in premap[crs]:
                if dfs(pre)==False:
                    return False
            visiting.remove(crs)
            visit.add(crs)
            res.append(crs)
            return True
        for c in range(numCourses):
            if dfs(c) == False:
                return []
        return res