class Solution:
    def isPalindrome(self, s: str) -> bool:
        s_join="".join(ch.lower()for ch in s if ch.isalnum())
        i=0
        j=len(s_join)-1
        while i<j:
            if s_join[i]!=s_join[j]:
                return False
            i+=1
            j-=1
        return True
        