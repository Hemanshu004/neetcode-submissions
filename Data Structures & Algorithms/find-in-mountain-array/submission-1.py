class Solution:
    def findInMountainArray(self, target: int, mountainArr: 'MountainArray') -> int:
        length=mountainArr.length()
        l,r=1,length-2
        while l<=r:
            m=(l+r)//2
            left,right,mid=mountainArr.get(m-1),mountainArr.get(m+1),mountainArr.get(m)
            if left<mid<right:
                l=m+1
            elif left>mid>right:
                r=m-1
            else:
                break
        peak=m

        #for left
        l,r=0,peak-1
        while l<=r:
            m=(l+r)//2
            val=mountainArr.get(m)
            if val<target:
                l=m+1
            elif val>target:
                r=m-1
            else:
                return m

        #for right
        l,r=peak,length-1
        while l<=r:
            mid=(l+r)//2
            val=mountainArr.get(mid)
            if val<target:
                r=mid-1
            elif val>target:
                l=mid+1
            else:
                return mid
        return -1
                




