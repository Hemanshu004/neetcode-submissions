class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        self.res=[]
        def dfs(i,remaining,subset):
            if i>=len(nums) or remaining<0:
                return 
            
            if remaining==0:
                self.res.append(subset.copy())
                return
            
            subset.append(nums[i])
            dfs(i,remaining-nums[i],subset)
            
            subset.pop()
            dfs(i+1,remaining,subset)
        
        dfs(0,target,[])
        return self.res
