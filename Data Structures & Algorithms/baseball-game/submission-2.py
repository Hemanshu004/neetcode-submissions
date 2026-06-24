class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack=[]
        res=0
        for x in operations:
            if x=="+":
                num=stack[-1]+stack[-2]
                stack.append(num)
            elif x=="D":
                num=stack[-1]*2
                stack.append(num)
            elif x=="C":
                stack.pop()
            
            else:
                stack.append(int(x))
        for n in stack:
            res+=n
        return  res