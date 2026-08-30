class Solution:
    def canTraverseAllPairs(self, nums: List[int]) -> bool:
        adj=[[]for i in range(len(nums))]
        visit=[False]*len(nums)
        for i in range(len(nums)):
            for j in range(len(nums)):
                if math.gcd(nums[i],nums[j])>1:
                    adj[i].append(j)
                    adj[j].append(i)
        

        def dfs(node):
            visit[node]=True
            for nei in adj[node]:
                if not visit[nei]:
                    dfs(nei)


    

        
        dfs(0)
        for node in visit:
            if not node:
                return False
        return True