class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        seen=defaultdict(dict)

        for i,num in enumerate(nums):
            if num in seen:
                return num
            seen[num]=i
        return -1

        