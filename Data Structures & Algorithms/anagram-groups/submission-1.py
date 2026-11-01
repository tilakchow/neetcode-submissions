class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        grp = {}
        for i in strs :
            lable = "".join(sorted(i))
            if lable not in grp :
                grp[lable] = []
            grp[lable].append(i)
        return list(grp.values())
             


