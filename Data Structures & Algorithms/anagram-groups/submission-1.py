class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        A_dict={}
        for s in strs:
            key=" ".join(sorted(s))
            if key not in A_dict:
                A_dict[key]=[]
            A_dict[key].append(s)
        return list(A_dict.values())