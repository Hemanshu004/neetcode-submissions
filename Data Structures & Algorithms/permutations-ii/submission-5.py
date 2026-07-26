class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        self.res=[]
        nums.sort()
        self.dfs(nums,[],[False]*len(nums))
        return self.res


    def dfs(self,nums,perm,pick):
        if len(perm)==len(nums):
            self.res.append(perm[:])
            return 
        
        for i in range(len(nums)):
            if pick[i]:
                continue
            
            if i>0 and nums[i]==nums[i-1] and not pick[i-1]:
                continue
            
            perm.append(nums[i])
            pick[i]=True
            self.dfs(nums,perm,pick)
            pick[i]=False
            perm.pop()
    