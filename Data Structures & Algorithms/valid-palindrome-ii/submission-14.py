class Solution:
    def validPalindrome(self, s: str) -> bool:
        def ispalindrome(i, j):
            while i < j:
                if s[i] != s[j]:
                    return False
                i += 1
                j -= 1
            return True  # ✅ This should be after the loop

        i = 0
        j = len(s) - 1
        while i < j:
            if s[i] != s[j]:
                # Try skipping one character either from the left or the right
                return ispalindrome(i + 1, j) or ispalindrome(i, j - 1)
            i += 1
            j -= 1
        return True
