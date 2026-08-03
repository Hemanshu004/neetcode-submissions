class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        dict={}
        for i,num in enumerate(nums):
            if num in dict and abs( dict[num]-i)<=k:
                return True
            dict[num]=i
        return False