class Solution:
    def romanToInt(self, s: str) -> int:
        #程序伪代码
        #遍历数组
        #if flag==1:
        #   res += 当前数-前一个数
        #   flag = 0
        #   continue
        #if 不是最后一个字符 and 当当前字母所表示的数小于下一个字母所表示的数时
        #    flag = 1
        #    continue
        #else
        #     res += 当前数所表示的数字
        roman2integer = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        flag = 0
        res = 0
        lens = len(s)
        for index in range(lens):
            if flag==1:
                res += roman2integer[s[index]] - roman2integer[s[index-1]]
                flag = 0
            elif index+1!=lens and roman2integer[s[index]] < roman2integer[s[index+1]]:
                flag = 1
                continue
            else:
                res += roman2integer[s[index]]
                
        return res

    # best
    class Solution:
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        a = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}        
        ans=0        
        for i in range(len(s)):            
            if i<len(s)-1 and a[s[i]]<a[s[i+1]]:                
                ans-=a[s[i]]
            else:
                ans+=a[s[i]]
        return ans
