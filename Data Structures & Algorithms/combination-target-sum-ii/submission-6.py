class Solution:
    def combinationSum2(self, can: List[int], target: int) -> List[List[int]]:
        res=[]
        can.sort()

        def dfs(i,remain,subset):
            if remain==0:
                res.append(subset[:])
                return 

            if i>=len(can) or remain<0:
                return
            
            subset.append(can[i])
            dfs(i+1,remain-can[i],subset)

            subset.pop()
            while i+1<len(can) and can[i]==can[i+1]:
                i+=1
            dfs(i+1,remain,subset)
        
        dfs(0,target,[])
        return res