class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        # [0]=[1]
        courses={i:[] for i in range(numCourses)}
        for x,y in prerequisites:
            courses[x].append(y)


        visit=set()
        def dfs(crs):
            if crs in visit:
                return False
            
            if courses[crs]==[]:
                return True
            visit.add((crs))

            for drs in courses[crs]:
                if not dfs(drs):
                    return False
            visit.remove(crs)
            courses[crs]=[]
            return True


        for crs in range(numCourses):
            if not dfs(crs):
                return False
        return True