class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res=[]
        path=[]
        def dfs(close,open):
            if n==open==close:
                res.append("".join(path))
                return 
            

            if open<n:
                path.append("(")
                dfs(close,open+1)
                path.pop()
            
            if close<open:
                path.append(")")
                dfs(close+1,open)
                path.pop()
        dfs(0,0)
        return res
            


