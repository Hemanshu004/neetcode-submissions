class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        mp=set()
        l=0
        for i in range(len(nums)):
            if i-l>k:
                mp.remove(nums[l])
                l+=1
            if nums[i] in mp :
                return True
            mp.add(nums[i])
        return False
            
