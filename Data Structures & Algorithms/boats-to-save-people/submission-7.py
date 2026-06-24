class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        l=0
        r=len(people)-1
        boat=0
        while l<=r:
            curr=limit
            curr-=people[r]
            r-=1
            boat+=1
            if l<=r and curr>=people[l]:
                l+=1
        return boat

