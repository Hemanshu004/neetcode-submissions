class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        premap={i:[] for i in range(numCourses)}
        for cors, pre in prerequisites:
            premap[cors].append(pre)

        visit=set()
        def dfs(cors):
            if cors in visit:
                return False
            if premap[cors]==[]:
                return True
            
            visit.add(cors)
            for pre in premap[cors]:
                if not dfs(pre):
                    return False
            visit.remove(cors)
            premap[cors]=[]
            return True
        
        for cors in range(numCourses):
            if not dfs(cors):
                return False
        return True