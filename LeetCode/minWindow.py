# target字典存储目标状态，d为当前转态，label存储当前标签。
# 时间复杂度O(m*n)，空间复杂度


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        label = []
        
        d = {}
        target = {}
        for ct in t:
            if ct in target:
                target[ct] += 1
            else:
                target[ct] = 1
                d[ct] = 0
                
        res = (0, len(s))
        flag = False
        
        for cs in range(len(s)):
            for ct in t:
                
                if ct==s[cs]:
                    label.append(cs)
                    d[ct] += 1
                    match = True
                    
                    while(match):
                        
                        for k in target.keys():
                            if d[k] >= target[k]:
                                continue
                            else:
                                match = False
                                break
                        else:
                            if res[1] - res[0] >= label[-1] - label[0]:
                                flag = True
                                res = (label[0], label[-1])
                            
                            d[s[label[0]]] -= 1
                            label = label[1:]
                            
                        
                    break
                        
        return s[res[0]: res[1]+1] if flag else ""
