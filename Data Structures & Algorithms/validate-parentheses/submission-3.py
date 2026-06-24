class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        for x in s:
            if x=="(" or x=="[" or x=="{":
                stack.append(x)
            else:
                if not stack:
                    return False
                if x==")" and stack[-1]!="(":
                    return False
                if x=="}" and stack[-1]!="{":
                    return False
                if x=="]" and stack[-1]!="[":
                    return False
                stack.pop()
        return len(stack)==0

            
            
                

