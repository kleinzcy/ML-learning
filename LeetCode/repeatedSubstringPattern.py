# 我的解法比较长，不知道为什么速度这么慢。没有重复的计算。
class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        for index in range(1,len(s)):
            if s[0]==s[index] and len(s)%index==0:
                for temp in range(index):
                    flag = 1
                    for j in range(1, len(s)//index):
                        if s[temp]!=s[temp+j*index]:
                            flag = 0
                            break
                            
                    if not flag:
                        break
                else:
                    return True
                
            elif index>int(len(s)/2):
                return False
            
        return False

# 利用python字符串乘法的特性，第三个方法则是利用子串是s的因子，降低时间复杂度。
class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        for l in range(1,len(s)//2+1):
            if s[:l] * (len(s)//l) == s:
                return True
        return False
        
class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        for l in range(1,len(s)//2+1):
            if len(s)%l==0 and s[:l] * (len(s)//l) == s:
                return True
        return False
                
