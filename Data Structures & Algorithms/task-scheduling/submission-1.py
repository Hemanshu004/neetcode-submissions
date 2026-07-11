class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count=[0]*26
        for task in tasks:
            count[ord(task)-ord('A')]+=1
        

        maxf=max(count)
        maxcount=0
        for i in count:
            if i==maxf:
                maxcount+=1
        

        time=(maxf-1)*(n+1)+maxcount
        return max(time,len(tasks))