class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        d={ch:i for i,ch in enumerate(order)}
        def in_order(w1,w2):
            n=min(len(w1),len(w2))
            for i in range(n):
                if w1[i]!=w2[i]:
                    return d[w1[i]]<d[w2[i]]
            
            return len(w1)<=len(w2)
        
        for i in range(len(words)-1):
            if not in_order(words[i],words[i+1]):
                return False
        return True 
