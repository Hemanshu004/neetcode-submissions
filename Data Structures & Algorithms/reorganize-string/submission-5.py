class Solution:
    def reorganizeString(self, s: str) -> str:
        count={}
        for ch in s:
            count[ch]=count.get(ch,0)+1
        maxheap=[]
        for char,cnt in count.items():
            maxheap.append([-cnt,char])
        
        heapq.heapify(maxheap)

        res=""
        prev=None
        while maxheap or prev:
            if prev and not maxheap:
                return ""
            
            cnt,char=heapq.heappop(maxheap)
            res+=char
            cnt+=1
            
            if prev:
                heapq.heappush(maxheap,prev)
                prev=None
            
            if cnt<0:
                prev=[cnt,char]
        return res
        

