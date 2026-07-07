class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!= len(t):
            return False
        Count = {}

        for i in range(len(s)):
            Count[s[i]] = 1 + Count.get(s[i],0)
        for j in range(len(t)):
            if Count.get(t[j],0) == 0 :
                return False
            Count[t[j]] = Count.get(t[j]) - 1     
        return sum(Count.values()) == 0