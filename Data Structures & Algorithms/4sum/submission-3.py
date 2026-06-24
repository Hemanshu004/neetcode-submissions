class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        res=[]
        for a in range(len(nums)):
            if a>0 and nums[a]==nums[a-1]:
                continue
            for d in range(len(nums)-1,a+2,-1):
                if d<len(nums)-1 and nums[d]==nums[d+1]:
                    continue
                b=a+1
                c=d-1
                while b<c:
                    four=nums[a]+nums[b]+nums[c]+nums[d]
                    if four <target:
                        b+=1
                    elif four>target:
                        c-=1
                    elif four==target:
                        res.append([nums[a],nums[b],nums[c],nums[d]])
                        b+=1
                        c-=1
                        while b<c and nums[b]==nums[b-1]:
                            b+=1
                        while b<c and nums[c]==nums[c+1]:
                            c-=1

        return res