class Solution:
    def calPoints(self, operations: List[str]) -> int:
        res=0
        stack=[]
        for x in operations:
            if x=="+":
                num=stack[-1]+stack[-2]
                stack.append(num)
            
            elif x=="C":
                stack.pop()
            
            elif x=="D":
                num=stack[-1]*2
                stack.append(num)
            else:
                num=int(x)
                stack.append(num)
        for i in stack:
            res+=i
        
        return res
            