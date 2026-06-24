class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        closetoopen={ ")" : "(", "]" : "[", "}" : "{" }
        for n in s:
            if n in closetoopen:
                if stack and stack[-1]==closetoopen[n]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(n)
        return True if not stack else False