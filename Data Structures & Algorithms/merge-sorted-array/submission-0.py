class Solution:
    def merge(self, num1: List[int], m: int, num2: List[int], n: int) -> None:
        # Start from the end of both arrays
        i = m - 1
        j = n - 1
        k = m + n - 1
        
        # Compare from the end and fill the largest element
        while i >= 0 and j >= 0:
            if num1[i] > num2[j]:
                num1[k] = num1[i]
                i -= 1
            else:
                num1[k] = num2[j]
                j -= 1
            k -= 1

       
        while j >= 0:
            num1[k] = num2[j]
            j -= 1
            k -= 1
