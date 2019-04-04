  def longestCommonPrefix(self, strs):
      if not strs: return ""
      s1 = min(strs)
      s2 = max(strs)
      for i,x in enumerate(s1):
          if x != s2[i]:
              return s2[:i]
      return s1
        
        
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if strs:
            res = strs[0]
        else:
            return ''
            
        for s in strs[1:]:
            for index in range(len(res)):
                if index + 1 <= len(s) and res[index]==s[index]:
                    pass
                else:
                    res = res[:index]
                    break
                    
        return res
