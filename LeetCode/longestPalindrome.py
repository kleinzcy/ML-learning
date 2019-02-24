# my solution: 8708ms, 6.5MB
# 暴力法
class Solution:
    def longestPalindrome(self, s: 'str') -> 'str':
        temp = []
        res_len = -1
        res = ""

        for idx in range(len(s)):
            temp = s[idx]
            if len(s)==1:
                return s
            for _c in s[idx + 1:]:
                temp += _c
                if res_len < len(temp) and temp == temp[::-1]:
                    res_len = len(temp)
                    res = temp
                    
        if not res and s:
            return s[0]
                    
        return res
