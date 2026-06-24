class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        grams={}
        for n in strs:
            key="".join(sorted(n))
            if key not in grams:
                grams[key]=[]
            grams[key].append(n)
        return list(grams.values())