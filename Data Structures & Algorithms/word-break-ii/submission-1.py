class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        cache={}
        word_s=set(wordDict)
        def dfs(i):
            if i==len(s):
                return [""]
            if i in cache:
                return cache[i]
            
            res=[]
            for j in range(i,len(s)):
                w=s[i:j+1]
                if w not in word_s:
                    continue
                
                strings=dfs(j+1)
                for substr in strings:
                    sentence=w
                    if substr:
                        sentence+=" "+substr
                    res.append(sentence)
            cache[i]=res
            return res
        return dfs(0)
                   
        