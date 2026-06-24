from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dict=defaultdict(list)
        for s in strs:
            sorted_word=''.join(sorted(s))
            dict[sorted_word].append(s)
        return list(dict.values())
