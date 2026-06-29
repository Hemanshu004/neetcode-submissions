class Solution:
    def findInMountainArray(self, target: int, mountainArr: 'MountainArray') -> int:
        l=1
        length=mountainArr.length()
        r=(length)-2
        while l<=r:
            m=(l+r)//2
            left,mid,right=mountainArr.get(m-1),mountainArr.get(m),mountainArr.get(m+1)
            if left<mid<right:
                l=m+1
            elif left>mid>right:
                r=m-1
            else:
                break
        peak=m
        r=peak-1
        l=0
        while l<=r:
            m=(l+r)//2
            mid=mountainArr.get(m)
            if mid>target:
                r=m-1
            elif mid<target:
                l=m+1
            else:
                return m
        
        l=peak
        r=length-1
        while l<=r:
            m=(l+r)//2
            mid=mountainArr.get(m)
            if mid==target:
                return m
            elif mid>target:
                l=m+1
            else:
                r=m-1
        return -1

        



