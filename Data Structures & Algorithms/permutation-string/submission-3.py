class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        st=set()
        n=len(s1)
        st.add("".join(sorted(s1)))
        l=0
        for r in range(len(s2)):
            window=s2[l:r+1]
            if len(window)>n:
                l+=1
                window=s2[l:r+1]
            sorted_window = "".join(sorted(window))
            if sorted_window in st:
                return True
        return False   
            