class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dict={}
        for num in nums:
            if num in dict:
                return True
            dict[num]=True
        return False