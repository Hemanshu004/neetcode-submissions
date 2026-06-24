class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        l=0
        r=len(nums)-1

        while l<r:
            m=(l+r)//2
            if nums[m]==target:
                return True
            
            if nums[m]==nums[l]==nums[r]:
                l+=1
                r-=1
            
            elif nums[l]<=nums[m]:
                if nums[l]<=target and target<=nums[m]:
                    r=m-1
                else:
                    l=m+1
            
            else:
                if nums[m]<=target and target<=nums[r]:
                    l=m+1
                else:
                    r=m-1
        return True if nums[l]==target else False