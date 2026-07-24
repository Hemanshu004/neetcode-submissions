class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res=[]
        pick=[False]*len(nums)
        perm=[]

        def dfs():
            if len(perm)==len(nums):
                res.append(perm[:])
                return
            

            for i in range(len(nums)):
                if pick[i]:
                    continue
                if i>0 and nums[i]==nums[i-1]and not pick[i-1]:
                    continue

                pick[i]=True
                perm.append(nums[i])
                dfs()
                pick[i]=False
                perm.pop()
            
        dfs()
        return res

        