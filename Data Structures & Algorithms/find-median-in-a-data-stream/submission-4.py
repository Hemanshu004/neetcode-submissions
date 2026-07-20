class MedianFinder:

    def __init__(self):
        self.arr=[]
        self.length=0

    def addNum(self, num: int) -> None:
        self.arr.append(num)
        self.arr.sort()
        self.length+=1

    def findMedian(self) -> float:
        if self.length%2==0:
            idx1=(self.length//2)-1
            idx2=(self.length//2)

            ans=(self.arr[idx1]+self.arr[idx2])/2
            return ans 
        else:
            idx=self.length//2
            return self.arr[idx]
            
        
        
        
        