class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        freq={}
        for s in nums:
            freq[s]=freq.get(s,0)+1
        return max(freq,key=freq.get)