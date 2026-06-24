class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        num={i:[] for i in range(numCourses)}
        for crs,dst in prerequisites:
            num[crs].append(dst)

        res=[]
        visit=set()
        def dfs(crs):
            if crs in visit:
                return False
            
            if num[crs]==[]:
                if crs not in res:
                    res.append(crs)
                return True

            visit.add(crs)
            for nei in num[crs]:
                if not dfs(nei):
                    return False
                
            visit.remove(crs)
            res.append(crs)
            num[crs]=[]
            return True

        for i in range(numCourses):
            if  dfs(i)== False:
                return []
        return res
            
