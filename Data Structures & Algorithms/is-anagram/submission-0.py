class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t) :
            False
        count_s = {}
        for ch in s :
            count_s[ch] = count_s.get(ch,0)+1
        count_t = {}    
        for ch in t :
            count_t[ch] = count_t.get(ch,0)+1
        return count_t == count_s             