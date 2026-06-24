class Solution:
    def isPalindrome(self, s: str) -> bool:
        s_spaces=s.replace(" ","")
        s_alpha=re.sub(r'[^A-Za-z0-9]', "",s_spaces).lower()
        left,right=0,len(s_alpha)-1
        while left<right:
            if s_alpha[left]!=s_alpha[right]:
                return False
            left +=1
            right -=1
        return True

       
