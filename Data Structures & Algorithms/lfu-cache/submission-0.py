class ListNode:

    def __init__(self, val, prev=None, next=None):
        self.val = val
        self.prev = prev
        self.next = next

class LinkedList:

    def __init__(self):
        self.left = ListNode(0)
        self.right = ListNode(0, self.left)
        self.left.next = self.right
        self.map = {}

    def length(self):
        return len(self.map)

    def pushRight(self, val):
        node = ListNode(val, self.right.prev, self.right)
        self.map[val] = node
        self.right.prev = node
        node.prev.next = node

    def pop(self, val):
        if val in self.map:
            node = self.map[val]
            next, prev = node.next, node.prev
            next.prev = prev
            prev.next = next
            self.map.pop(val, None)

    def popLeft(self):
        res = self.left.next.val
        self.pop(self.left.next.val)
        return res

    def update(self, val):
        self.pop(val)
        self.pushRight(val)

class LFUCache:

    def __init__(self, capacity: int):
            self.cap=capacity
            self.lfucnt=0
            self.valmap={}
            self.countmap=defaultdict(int)
            self.listmap=defaultdict(LinkedList)

    def counter(self, key):
        cnt=self.countmap[key]
        self.countmap[key] +=1
        self.listmap[cnt].pop(key)
        self.listmap[cnt+1].pushRight(key)

        if cnt==self.lfucnt and self.listmap[cnt].length()==0:
            self.lfucnt +=1


    def get(self, key: int) -> int:
        if key not in self.valmap:
            return -1
        self.counter(key)
        return self.valmap[key]

    def put(self, key: int, value: int) -> None:
        if self.cap==0:
            return 

        if key not in self.valmap and len(self.valmap)==self.cap:
            res=self.listmap[self.lfucnt].popLeft()
            self.valmap.pop(res)
            self.countmap.pop(res)

        self.valmap[key]=value
        self.counter(key)
        self.lfucnt=min(self.lfucnt,self.countmap[key])