class ListNode:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.freq = 1
        self.prev = None
        self.next = None

class LinkedList:
    def __init__(self):
        self.left = ListNode(0, 0)
        self.right = ListNode(0, 0)
        self.left.next = self.right
        self.right.prev = self.left
        self.size = 0

    def length(self):
        return self.size

    def pushRight(self, node):
        prev = self.right.prev
        prev.next = node
        node.prev = prev
        node.next = self.right
        self.right.prev = node
        self.size += 1

    def pop(self, node):
        prev, next = node.prev, node.next
        prev.next = next
        next.prev = prev
        node.prev = None
        node.next = None
        self.size -= 1

    def popLeft(self):
        if self.length() == 0:
            return None
        node = self.left.next
        self.pop(node)
        return node


class LFUCache:
    def __init__(self, capacity: int):
        self.Nodemap={}
        self.listmap=defaultdict(LinkedList)
        self.cap=capacity
        self.lfucnt=0


    def counter(self,node):
        cnt=node.freq
        self.listmap[cnt].pop(node)

        if cnt==self.lfucnt and self.listmap[self.lfucnt].length()==0:
            self.lfucnt+=1
        
        node.freq+=1
        self.listmap[cnt+1].pushRight(node)



    def get(self, key: int) -> int:
        if key not in self.Nodemap:
            return -1
        node=self.Nodemap[key]
        self.counter(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        if self.cap==0:
            return 
        
        if key in self.Nodemap:
            node=self.Nodemap[key]
            node.val=value
            self.counter(node)
            return 
        
        if len(self.Nodemap)==self.cap:
            node=self.listmap[self.lfucnt].popLeft()
            self.Nodemap.pop(node.key)
        
        node=ListNode(key,value)
        self.Nodemap[key]=node
        self.listmap[1].pushRight(node)
        self.lfucnt=1
        

            

        
        


# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)