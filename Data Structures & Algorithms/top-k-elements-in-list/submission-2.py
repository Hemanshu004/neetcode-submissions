class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq={}
        res=[]
        for num in nums:
            freq[num]=freq.get(num,0)+1
        
        while k:
            max_key=max(freq,key=freq.get)
            res.append(max_key)
            freq.pop(max_key,None)
            k-=1
        return res
            