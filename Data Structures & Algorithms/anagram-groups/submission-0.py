class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
       Str= {}
       for str in strs:
          key = ''.join(sorted(str))
          if key in Str:
            Str[key].append(str)
          else:
            Str[key] = [str]
       return list(Str.values())
 