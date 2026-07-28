class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        total=sum(nums)
        if total%k!=0:
            return False
        
        target=total//k
        nums.sort(reverse=True)
        pick=[False]*len(nums)
        
        def dfs(i,subset,k):
            if k==0:
                return True
            
            if subset==target:
                return dfs(0,0,k-1)
                 
            
            for j in range(i,len(nums)):
                if not pick[j] and subset+nums[j]<=target:
                    pick[j]=True
                    if dfs(j+1,subset+nums[j],k):
                        return True
                    pick[j]=False
                
                    if subset==0:
                        return False
            return False
            
        return dfs(0,0,k)