from collections import Counter
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        h=len(nums)/3
        res=[]
        count=Counter(nums)
        for k,v in count.items():
            if v>h:
                res.append(k)
        return res
        