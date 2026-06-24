class Solution:
    def simplifyPath(self, path: str) -> str:
        stack=[]
        paths=path.split("/")
        for ch in paths:
            if ch=="" or ch==".":
                continue
            elif ch=="..":
                if stack:
                    stack.pop()
            else:
                stack.append(ch)
        return "/"+"/".join(stack)