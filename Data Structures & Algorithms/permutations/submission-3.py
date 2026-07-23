class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        self.res=[]
        self.dfs(nums,[],[False]*len(nums))
        return self.res
    

    def dfs(self,nums,perm,pick):
        if len(perm)==len(nums):
            self.res.append(perm[:])
            return 
        
        for i in range(len(nums)):
            if not pick[i]:
                perm.append(nums[i])
                pick[i]=True
                self.dfs(nums,perm,pick)
                perm.pop()
                pick[i]=False
        
