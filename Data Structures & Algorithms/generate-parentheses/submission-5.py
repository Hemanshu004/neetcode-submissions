class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res=[]
        def dfs(close,open,path):
            if n==open==close:
                res.append("".join(path))
                return 
            

            if open<n:
                path.append("(")
                dfs(close,open+1,path)
                path.pop()
            
            if close<open:
                path.append(")")
                dfs(close+1,open,path)
                path.pop()

        dfs(0,0,[])
        return res
            


