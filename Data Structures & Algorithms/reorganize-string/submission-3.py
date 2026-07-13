class Solution:
    def reorganizeString(self, s: str) -> str: 
        count=Counter(s)
        maxheap=[]
        rearrange_str=""
        for ch,i in count.items():
            maxheap.append([i*(-1),ch])
        heapq.heapify(maxheap)

        prev=None
        while maxheap or prev:
            if prev and not maxheap:
                return ""

            i,ch=heapq.heappop(maxheap)
            if rearrange_str and  rearrange_str[-1]==ch:
                return ""
            else:
                rearrange_str+=ch

            if prev:
                heapq.heappush(maxheap,prev)
                prev=None

            if i+1<0:
                prev=[i+1,ch]

        
        return rearrange_str


        

