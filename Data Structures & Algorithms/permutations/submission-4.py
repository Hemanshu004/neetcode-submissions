class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        self.res=[]
        self.dfs(nums,[],[False]*len(nums))
        return self.res
        
        
    def dfs(self,nums,subset,pick):
        if len(subset)==len(nums):
            self.res.append(subset[:])
            return 
            
        for i in range(len(nums)):
            if not pick[i]:
                subset.append(nums[i])
                pick[i]=True
                self.dfs(nums,subset,pick)
                subset.pop()
                pick[i]=False
        
                