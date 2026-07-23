class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        pick = [False] * len(nums)

        def dfs(perm):
            if len(perm) == len(nums):
                res.append(perm[:])
                return

            for i in range(len(nums)):
                # Already used in the current permutation
                if pick[i]:
                    continue

                # Skip duplicate numbers
                if i > 0 and nums[i] == nums[i - 1] and not pick[i - 1]:
                    continue

                perm.append(nums[i])
                pick[i] = True

                dfs(perm)

                perm.pop()
                pick[i] = False

        dfs([])
        return res