class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
       seen={}
       for i,num in enumerate(numbers):
        num1=target-num
        if num1 in seen and num1<num:
            return [seen[num1]+1,i+1]
        seen[num]=i
                