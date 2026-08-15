class Solution:
    def check(self,s1,s2):
            length=min(len(s1),len(s2)) 
            n=0
            for i in range(length):
                if s1[i]!=s2[i]:
                    n+=1    
                if n>1:
                    break
            if n==1:
                return True
            else:
                return False    
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        adj=defaultdict(list)
        for ch in wordList:
            if self.check(beginWord,ch):
                adj[beginWord].append(ch)
                adj[ch].append(beginWord)
        for i in range(len(wordList)):
            for j in range(i + 1, len(wordList)):
                if self.check(wordList[i], wordList[j]):
                    adj[wordList[i]].append(wordList[j])
                    adj[wordList[j]].append(wordList[i])
            
        q=deque()
        visit=set()
        q.append((beginWord,1))
        visit.add(beginWord)
        while q:
            node,steps=q.popleft()
            if node==endWord:
                return steps
            for nei in adj[node]:
                if nei not in visit:
                    q.append((nei,steps+1))
                    visit.add(nei)
        return 0
            
            

