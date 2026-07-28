class TreeNode:
    def __init__(self,key,val):
        self.key=key
        self.val=val
        self.next=None
        self.prev=None


class LRUCache:

    def __init__(self, capacity: int):
        self.cap=capacity
        self.left=TreeNode(0,0)
        self.right=TreeNode(0,0)
        self.left.next=self.right
        self.right.prev=self.left
        self.Nodemap={}

    def remove(self,node):
        prev,nxt=node.prev,node.next
        prev.next=nxt
        nxt.prev=prev

    def add(self,node):
        prev=self.right.prev
        prev.next=node
        self.right.prev=node
        node.prev=prev
        node.next=self.right

    def get(self, key: int) -> int:
        if key in self.Nodemap:
            self.remove(self.Nodemap[key])
            self.add(self.Nodemap[key])
            return self.Nodemap[key].val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.Nodemap:
            self.remove(self.Nodemap[key])
        self.Nodemap[key]=TreeNode(key,value)
        self.add(self.Nodemap[key])

        if len(self.Nodemap)>self.cap:
            lfu=self.left.next
            self.remove(self.Nodemap[lfu.key])
            del self.Nodemap[lfu.key]



        
