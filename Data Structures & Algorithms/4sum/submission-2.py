class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        res=set()
        for a in range(len(nums)):
            for d in range(len(nums)-1,a+2,-1):
                b=a+1
                c=d-1
                while b<c:
                    four=nums[a]+nums[b]+nums[c]+nums[d]
                    if four <target:
                        b+=1
                    elif four>target:
                        c-=1
                    elif four==target:
                        res.add((nums[a],nums[b],nums[c],nums[d]))
                        b+=1
                        c-=1
        return[list(i) for i in res]