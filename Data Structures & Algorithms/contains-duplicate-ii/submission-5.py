class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        map=defaultdict()
        for i,n in enumerate(nums):
            if n in map:
                if abs(map[n]-i)<=k:
                    return True
            map[n]=i
        return False