class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans=[]
        ans1=[]
        for i in range(len(nums)):
            ans.append(nums[i])
            ans1.append(nums[i])
        return ans+ans1
