class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        emailIdx={}
        emails=[]
        emailToAcc={}
        
        m=0
        for accid , a in enumerate(accounts):
            for i in range(1,len(a)):
                email=a[i]
                if email in emails:
                    continue
                
                emails.append(email)
                emailIdx[email]=m
                emailToAcc[m]=accid
                m+=1


        adj=[[] for _ in range(m)]
        for a in accounts:
            for i in range(2,len(a)):
                id1=emailIdx[a[i]]
                id2=emailIdx[a[i-1]]
                adj[id1].append(id2)
                adj[id2].append(id1)
            
        
        emailGroup=defaultdict(list)
        visited=[False]*m
        def dfs(node,accid):
            visited[node]=True
            emailGroup[accid].append(emails[node])
            for nei in adj[node]:
                if not visited[nei]:
                    dfs(nei,accid)
        
        for i in range(m):
            if not visited[i]:
                dfs(i,emailToAcc[i])
        
        res=[]
        for accid in emailGroup:
            name=accounts[accid][0]
            res.append([name]+sorted(emailGroup[accid]))
        return res
            
        



