class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        repeat = 0
        if s=='':
            if p=='':
                return True
            else:
                return False

        for idx1, c in enumerate(p):
            if c==s[0] or c=='.':
                success = 1
                for idx2 in range(1, len(s)):
                    idxp = idx1 + idx2 - repeat
                    if idxp < 0 or idxp >= len(p):
                        break
                    if p[idxp]==s[idx2] or p[idxp]=='.':
                        success += 1
                    elif p[idxp]=='*' and (p[idxp-1]==s[idx2] or (p[idxp-1]=='.' and s[idx2]==s[idx2-1])):
                        # 字符重复，repeat加一，记录重复字符数。
                        repeat += 1
                        success += 1
                    elif p[idxp]=='*' and idxp+1 < len(p) and (p[idxp + 1]==s[idx2] or p[idxp+1]=='.') :
                        # 字符不重复
                        repeat -= 1
                        success += 1
                        
                if success==len(s):
                    return True
                    
        return False
