class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        close={ ")" : "(", "]" : "[", "}" : "{" }
        for ch in s:
            if ch in close:
                if stack and stack[-1]==close[ch]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(ch)
        return True if not stack else False
        