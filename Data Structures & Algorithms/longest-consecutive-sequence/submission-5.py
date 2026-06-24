class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        numset=set(nums)
        res=0
        for num in numset:
            if (num-1) not in numset:
                length=1
                while num+1 in numset:
                    length+=1
                    num=num+1
                res=max(length,res)
        return res