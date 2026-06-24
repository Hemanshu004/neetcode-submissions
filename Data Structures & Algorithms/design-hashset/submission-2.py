class MyHashSet:
    def __init__(self):
        self.size=10000;
        self.buckets=[[] for _ in range(self.size)]
    
    def _hash(self,key):
        return key % self.size
    
    def add(self,key):
        bucket_index=self._hash(key)
        bucket=self.buckets[bucket_index]
        if key not in bucket:
            bucket.append(key)
        
    def remove(self,key):
        bucket_index=self._hash(key)
        bucket=self.buckets[bucket_index]
        if key in bucket:
            bucket.remove(key)
    
    def contains(self,key):
        bucket_index=self._hash(key)
        return key in self.buckets[bucket_index]
