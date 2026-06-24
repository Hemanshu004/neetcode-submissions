class Solution:
    def maxArea(self, heights: List[int]) -> int:
        i=0
        j=len(heights)-1
        max_height = 0
        while i<j:
            curr=min(heights[i],heights[j])*(j-i)
            max_height=max(curr,max_height)
            if heights[i]<=heights[j]:
                i+=1
            elif heights[j]<heights[i]:
                j-=1
        return max_height   
