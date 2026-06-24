class FreqStack:

    def __init__(self):
        self.stack=[]
        self.freq=defaultdict(int)

    def push(self, val: int) -> None:
        self.stack.append(val)
        self.freq[val]+=1

    def pop(self) -> int:
        max_freq=max(self.freq.values())
        i=len(self.stack)-1
        while self.freq[self.stack[i]]!=max_freq:
            i-=1
        self.freq[self.stack[i]] -=1
        return self.stack.pop(i)



        


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()