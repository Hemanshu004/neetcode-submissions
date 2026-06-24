class FreqStack:

    def __init__(self):
        self.cnt={}
        self.stacks=[[]]

    def push(self, val: int) -> None:
        valcnt=self.cnt.get(val,0)+1
        self.cnt[val]=valcnt
        if valcnt==len(self.stacks):
            self.stacks.append([])
        self.stacks[valcnt].append(val)

    def pop(self) -> int:
        res=self.stacks[-1].pop()
        self.cnt[res]-=1
        if not self.stacks[-1]:
            self.stacks.pop()
        return res


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()