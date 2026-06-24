class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        res=[]
        nums.sort()
        n=len(nums)
        for a in range(n):
            if a>0 and nums[a]==nums[a-1]:
                continue
            
            for b in range(n-1,a+2,-1):
                if b<n-1 and nums[b]==nums[b+1]:
                    continue

                l=a+1
                r=b-1
                while l<r:
                    sun=nums[a]+nums[b]+nums[l]+nums[r]
                    if sun<target:
                        l+=1
                    elif sun>target:
                        r-=1
                    elif sun==target:
                        res.append([nums[a],nums[b],nums[l],nums[r]])
                        l+=1
                        r-=1

                        while l<r and nums[l]==nums[l-1]:
                            l+=1
                        while l<r and nums[r]==nums[r+1]:
                            r-=1
        return res






