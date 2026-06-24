class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dict1=defaultdict()
        for i in range(len(nums)):
            if nums[i] in dict1:
                return True
            dict1[nums[i]]=True
        return False