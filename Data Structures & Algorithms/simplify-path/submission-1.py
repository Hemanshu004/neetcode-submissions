class Solution:
    def simplifyPath(self, path: str) -> str:
        string=path.split("/")
        stack=[]
        for s in string:
            if s=="" or s==".":
                continue
            elif s=="..":
                if stack:
                    stack.pop()
            else:
                stack.append(s)
            
        return "/"+"/".join(stack)

