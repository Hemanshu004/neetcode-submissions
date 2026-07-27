class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        total=sum(nums)
        if total%k!=0:
            return False
        
        nums.sort(reverse=True)
        pick=[False]*len(nums)
        target=total//k
        def backtrack(i,subset,k):
            if k==0:
                return True
            
            if subset==target:
                return backtrack(0,0,k-1)
            
            for j in range(i,len(nums)):
                if pick[j] or subset+nums[j]>target:
                    continue
                pick[j]=True
                if backtrack(j+1,subset+nums[j],k):
                    return True
                pick[j]=False
                if subset==0:
                    return False
            return False
        
        return backtrack(0,0,k)
