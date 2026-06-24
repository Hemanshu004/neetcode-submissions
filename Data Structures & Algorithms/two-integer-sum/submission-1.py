class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen={}
        for i,val in enumerate(nums):
            ch=target-val
            if ch in seen:
                return[seen[ch],i]
            seen[val]=i