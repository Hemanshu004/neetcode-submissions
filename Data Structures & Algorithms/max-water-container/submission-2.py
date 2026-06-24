class Solution:
    def maxArea(self, heights: List[int]) -> int:
        i=0
        j=len(heights)-1
        max_water=0
        while i<j:
            current_water=(j-i)*min(heights[i],heights[j])
            max_water=max(current_water,max_water)
            if heights[j]<heights[i]:
                j-=1
            else:
                i+=1
        return max_water