class Solution:
    def reorganizeString(self, s: str) -> str:
        maxheap=[]
        count=Counter(s)
        for ch,cnt in count.items():
            maxheap.append([-cnt,ch])
        
        heapq.heapify(maxheap)
        res=""
        prev=None
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


        