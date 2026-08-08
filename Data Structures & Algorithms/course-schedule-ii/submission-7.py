class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        Courses={i:[] for i in range(numCourses)}
        for x,y in prerequisites:
            Courses[x].append(y)


        visit=set()
        res=[]
        def dfs(crs):
            if crs in visit:
                return False

            if Courses[crs]==[]:
                if crs not in res:
                    res.append(crs)
                return True
            visit.add(crs)
            for drs in Courses[crs]:
                if not dfs(drs):
                    return False
            
            visit.remove(crs)
            res.append(crs)
            Courses[crs]=[]
            return True
        
        for c in range(numCourses):
            if not dfs(c):
                return []
        return res
            
