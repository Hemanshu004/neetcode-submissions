class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        closeToOpen = { ")" : "(", "]" : "[", "}" : "{" }
        for x in s:
            if x in closeToOpen:
                if stack and stack[-1]==closeToOpen[x]:
                    stack.pop()
                else:
                    return False
            
            else:
                stack.append(x)
        
        return True if not stack else False


            
            
                

