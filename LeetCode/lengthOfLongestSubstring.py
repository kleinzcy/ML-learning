# my python solution
class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        res = -1
        if len(s)==0:
            return 0
        for idx in range(len(s)):
            _temp = 1
            for _c in s[(idx + 1):]:
                if _c in s[idx: idx + _temp]:
                    break
                _temp += 1
            if _temp > res:    
                res = _temp
                
        return res
        
# good solution        
class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        st = {}
        i, ans = -1, 0
        for j in range(len(s)):
            if s[j] in st:
                i = max(st[s[j]], i)
            ans = max(ans, j - i)
            st[s[j]] = j
        return ans;
