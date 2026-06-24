class Solution:
    def decodeString(self, s: str) -> str:
        num=0
        curr=""
        stack=[]
        for ch in s:
            if ch.isdigit():
                num=num*10+int(ch)
            elif ch.isalpha():
                curr+=ch
            elif ch=="[":
                stack.append((num,curr))
                num=0
                curr=""
            elif ch=="]":
                prevnum,prevch=stack.pop()
                curr= prevch + prevnum * curr

        return curr
            