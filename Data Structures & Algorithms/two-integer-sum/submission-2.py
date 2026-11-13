class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen={}
        for i, x in enumerate(nums):
            diff=target-x
            if diff in seen and seen[diff]!=i:
                return [seen[diff],i]
            seen[x]=i
        