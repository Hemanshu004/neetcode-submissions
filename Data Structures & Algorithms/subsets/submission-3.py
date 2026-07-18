class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def dfs(i,subset):
            if i==len(nums):
                return [subset.copy()]
            
            subset.append(nums[i])
            left=dfs(i+1,subset)

            subset.pop()
            right=dfs(i+1,subset)

            return left+right
        return dfs(0,[])
