class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack=[]
        for c in asteroids:
            if c>0:
                stack.append(c)

            else:
                while stack and stack[-1]>0 and abs(c)>stack[-1] :
                    stack.pop()
                
                if not stack or stack[-1]<0:
                    stack.append(c)
                
                elif stack and stack[-1]>0 and abs(c)==stack[-1] :
                    stack.pop()
        return stack