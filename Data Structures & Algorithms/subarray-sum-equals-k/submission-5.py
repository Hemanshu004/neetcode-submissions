class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        res=cur=0
        prefix_sum={0:1}
        for i in range(len(nums)):
            cur +=nums[i]
            diff=cur-k

            res+=prefix_sum.get(diff,0)
            prefix_sum[cur]=prefix_sum.get(cur,0)+1
        return res