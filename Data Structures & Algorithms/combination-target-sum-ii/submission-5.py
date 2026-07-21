class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res=[]
        candidates.sort()
        def dfs(i,remaining,subset):
            if remaining==0:
                res.append(subset.copy())
                return 

            if i>=len(candidates) or remaining<0:
                return 
            
            subset.append(candidates[i])
            dfs(i+1,remaining-candidates[i],subset)

            subset.pop()
            while i+1<len(candidates) and candidates[i]==candidates[i+1]:
                i+=1
            dfs(i+1,remaining,subset)
        
        dfs(0,target,[])
        return res