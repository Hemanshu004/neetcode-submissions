class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        self.res=[]
        def dfs(i,remain,subset):
            if i>=len(nums) or remain<0:
                return 
            
            if remain==0:
                self.res.append(subset[:])
                return
            
            subset.append(nums[i])
            dfs(i,remain-nums[i],subset)

            subset.pop()
            dfs(i+1,remain,subset)
        
        dfs(0,target,[])
        return self.res
