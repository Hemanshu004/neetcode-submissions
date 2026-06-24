class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count=[[]for _ in range(len(nums)+1)]
        dict={}

        for i in range(len(nums)):
            dict[nums[i]]=dict.get(nums[i],0)+1
        
        for i ,v in dict.items():
            count[v].append(i)

        res=[]
        for i in range(len(count)-1,0,-1):
            for n in count[i]:
                res.append(n)
                if len(res)==k:
                    return res
        