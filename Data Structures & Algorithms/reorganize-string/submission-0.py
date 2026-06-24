class Solution:
    def reorganizeString(self, s: str) -> str:
        sdict=Counter(s)
        heap = [[-freq, ch] for ch, freq in sdict.items()]
        heapq.heapify(heap)
        res=[]
        prev=None
        res=""
        while heap or prev:
            if prev and not heap:
                return ""
            cnt,ch=heapq.heappop(heap)
            res +=ch
            cnt+=1

            if prev:
                heapq.heappush(heap,prev)
                prev= None
            if cnt!=0:
                prev=[cnt,ch]
            
        return res