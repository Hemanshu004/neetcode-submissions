class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        maxheap = []

        for cnt, char in [(a, 'a'), (b, 'b'), (c, 'c')]:
            if cnt > 0:
                heapq.heappush(maxheap, [-cnt, char])
        res=""
        prev=None
        while maxheap:
            cnt,char=heapq.heappop(maxheap)
            
            if len(res)>=2 and  char==res[-1] and char==res[-2]:
                if not maxheap:
                    break
                cnt2,char2=heapq.heappop(maxheap)
                res+=char2
                cnt2+=1
                
                if cnt2<0:
                    heapq.heappush(maxheap,[cnt2,char2])
                heapq.heappush(maxheap,[cnt,char])
            else:
                res+=char
                cnt+=1
                if cnt<0:
                    heapq.heappush(maxheap,[cnt,char])
        return res


            

            


