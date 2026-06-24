class MyHashMap:

    def __init__(self):
        self.size=1000
        self.data=[[]for i in range(self.size)]
    def hash(self,key):
        return key % self.size

    def put(self, key: int, value: int) -> None:
        idx=self.hash(key)
        bucket=self.data[idx]
        for i,(k,v)in enumerate (bucket):
            if k==key:
                bucket[i]=(key,value)
                return 
        bucket.append((key,value))
    def get(self, key: int) -> int:
        idx=self.hash(key)
        bucket=self.data[idx]
        for k,v in bucket:
            if k==key:
                return v
        return -1        

    def remove(self, key: int) -> None:
        idx=self.hash(key)
        bucket=self.data[idx]
        for i,(k,v)in enumerate (bucket):
            if k==key:
                bucket.pop(i)
                return 




# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)