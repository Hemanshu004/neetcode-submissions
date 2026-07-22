class Solution:
    def reorganizeString(self, s: str) -> str:
        count={}
        for ch in s:
            count[ch]=count.get(ch,0)+1
        
        maxheap=[[-cnt,ch] for ch,cnt in count.items()]
        prev=None
        res=""
        heapq.heapify(maxheap)

        while maxheap or prev:
            if prev and not maxheap:
                return ""
            
            cnt,ch=heapq.heappop(maxheap)
            res+=ch
            cnt+=1
            
            if prev:
                heapq.heappush(maxheap,prev)
                prev=None

            if cnt<0:
                prev=[cnt,ch]
        return res
