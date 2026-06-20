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
                stack.append((curr,num))
                curr=""
                num=0
            elif ch=="]":
                char,numm=stack.pop()
                curr=char+(numm*curr)
        return curr

