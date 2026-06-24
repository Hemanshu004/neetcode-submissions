import ast

class Solution:
    def twoSum(self, nums, target):
        dict = {}
        for i, num in enumerate(nums):
            ele = target - num
            if ele in dict:
                return [dict[ele], i]
            dict[num] = i
        return []

