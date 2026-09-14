class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        
        adj=defaultdict(list)
        wordList.append(beginWord)
        for word in wordList:
            for j in range(len(word)):
                pattern=word[:j]+ "*" + word[j+1:]
                adj[pattern].append(word)
        
        q=deque([(beginWord,1)])
        visit=set([beginWord])
        while q:
            node,steps=q.popleft()
            if node==endWord:
                return steps
            
            for j in range(len(node)):
                pattern=node[:j]+"*"+node[j+1:]

                for nei in adj[pattern]:
                    if nei not in visit:
                        visit.add(nei)
                        q.append((nei,steps+1))
        return 0
                        
                    

            
        

            

        
