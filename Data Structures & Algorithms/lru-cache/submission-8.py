class TreeNode:
    def __init__(self,key,val):
        self.val=val
        self.key=key
        self.next=None
        self.prev=None


class LRUCache:
    def __init__(self, capacity: int):
        self.cap=capacity
        self.Nodemap={}
        self.left=TreeNode(0,0)
        self.right=TreeNode(0,0)
        self.left.next=self.right
        self.right.prev=self.left
    
    def remove(self,node):
        tmp,tmp2=node.next,node.prev
        node.next.prev=tmp2
        node.prev.next=tmp

    def add(self,node):
        prev=self.right.prev
        nxt=self.right
        prev.next=node
        nxt.prev=node
        node.next,node.prev=nxt,prev
        


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
            lru=self.left.next
            self.remove(lru)
            del self.Nodemap[lru.key]


