class Solution:
    def decodeString(self, s: str) -> str:
        stack=[]
        stack_k=[]
        cur=""
        k=0
        for c in s:
            if c.isdigit():
                k=k*10+int(c)
            elif c=="[":
                stack.append(cur)
                stack_k.append(k)
                k=0
                cur=""
            elif c=="]":
                temp=cur
                count=stack_k.pop()
                cur=stack.pop()
                cur+=temp*count
            else:
                cur +=c
        return cur
