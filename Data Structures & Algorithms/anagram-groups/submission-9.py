class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram={}
        for s in strs:
            sorted_ana="".join(sorted(s))
            if sorted_ana not in anagram:
                anagram[sorted_ana]=[]
            anagram[sorted_ana].append(s)
        return [value for value in anagram.values()]