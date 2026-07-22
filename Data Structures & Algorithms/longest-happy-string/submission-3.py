class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        maxheap = []
        for cnt, char in [(a, 'a'), (b, 'b'), (c, 'c')]:
            if cnt > 0:
                heapq.heappush(maxheap, [-cnt, char])

        res=""
        while maxheap:
            cnt,ch=heapq.heappop(maxheap)
            if len(res)>1 and res[-1]==res[-2]==ch:
                if not maxheap:
                    break
                cnt2,ch2=heapq.heappop(maxheap)
                res+=ch2
                cnt2+=1 

                if cnt2<0:
                    heapq.heappush(maxheap,[cnt2,ch2])
                heapq.heappush(maxheap,[cnt,ch])
            else:
                res+=ch
                cnt+=1
                if cnt<0:
                    heapq.heappush(maxheap,[cnt,ch])
        return res
            

        
            


