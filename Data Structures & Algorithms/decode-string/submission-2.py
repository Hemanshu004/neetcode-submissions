class Solution:
    def decodeString(self, s: str) -> str:
        num=0
        cur=""
        stack=[]
        for ch in s:
            if ch.isdigit():
                num=num*10+int(ch)
            elif ch.isalpha():
                cur +=ch
            elif ch=="[":
                stack.append((num,cur))
                cur=""
                num=0
            elif ch=="]":
                prevnum,prevch=stack.pop()
                cur=prevch + prevnum * cur
        return cur