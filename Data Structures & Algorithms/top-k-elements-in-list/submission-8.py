from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        Count=Counter(nums)
        return[num for num, freq in Count.most_common(k)]
 

            