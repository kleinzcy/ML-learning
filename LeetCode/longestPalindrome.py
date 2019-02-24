# my solution: 8708ms, 6.5MB
# 暴力法 时间复杂度O(n^3)
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

# solution 2,时间复杂度O(n^2),空间复杂度O(n)，1544
class Solution:
    def longestPalindrome(self, s: 'str') -> 'str':
        # 动态规划解法
        res = ""
        lens = len(s)
        if lens==0:
            return res
        
        indexlist = [(i,i) for i in range(lens)]
        indexlist_lens = [1] * lens
        indexlist_even = [(i,i) for i in range(lens)]
        indexlist_lens_even = [1] * lens
        
        for ind in range(lens):
            left, right = indexlist[ind]
            while(True):
                _left = left - 1
                _right = right + 1
                if _left >= 0 and _right < lens and s[_left] == s[_right]:
                    indexlist[ind] = (_left, _right)
                    indexlist_lens[ind] = _right - _left + 1
                    left, right = _left, _right
                else:
                    break
                        
            left, right = indexlist_even[ind]
            if right + 1 < lens and s[left] == s[right + 1]:
                right += 1
                indexlist_even[ind] = (left, right)
                indexlist_lens_even[ind] = right - left + 1
                while(True):
                    _left = left - 1
                    _right = right + 1
                    if _left >= 0 and _right < lens and s[_left] == s[_right]:
                        indexlist_even[ind] = (_left, _right)
                        indexlist_lens_even[ind] = _right - _left + 1
                        left, right = _left, _right
                    else:
                        break
                            
        max1, max2 = max(indexlist_lens), max(indexlist_lens_even)
        if max1 >= max2:
            left, right = indexlist[indexlist_lens.index(max1)]
            if left != right:
                res = s[left:right + 1]
            else:
                res = s[left]           
        else:
            left, right = indexlist_even[indexlist_lens_even.index(max2)]
            res = s[left:right + 1]

        return res
  
# solution 3: 时间复杂度O(n^2)，空间复杂度O(1), 1236ms, 6.4MB
# 相比如solution 2，节省了很多空间。速度也提高
class Solution:
    def longestPalindrome(self, s: 'str') -> 'str':
        res = ""
        lens = len(s)
        if lens==0:
            return res
        
        longest = 0

        for ind in range(lens):
            left, right = ind,ind
            while(True):
                _left = left - 1
                _right = right + 1
                if _left >= 0 and _right < lens and s[_left] == s[_right]:
                    _lens = _right - _left + 1
                    if _lens > longest:
                        longest = _lens
                        res = s[_left:_right+1]
                        
                    left, right = _left, _right
                else:
                    break
                        
            left, right = ind, ind
            if right + 1 < lens and s[left] == s[right + 1]:
                right += 1
                _lens = right - left + 1
                if _lens > longest:
                    longest = _lens
                    res = s[left: right+1]
                    
                while(True):
                    _left = left - 1
                    _right = right + 1
                    if _left >= 0 and _right < lens and s[_left] == s[_right]:
                        _lens = _right - _left + 1
                        if _lens > longest:
                            longest = _lens
                            res = s[_left:_right+1]
                            
                        left, right = _left, _right
                    else:
                        break
        if longest==0:
            return s[0]                    

        return res

    
 # solution 4:和solution3基本相同，只是减少了字符串的切片操作。
class Solution:
    def longestPalindrome(self, s: 'str') -> 'str':
        res = ""
        lens = len(s)
        if lens==0:
            return res
        
        longest = 0

        for ind in range(lens):
            left, right = ind,ind
            while(True):
                left = left - 1
                right = right + 1
                if left >= 0 and right < lens and s[left] == s[right]:                     
                    continue
                else:
                    left += 1
                    right -= 1
                    break
                        
            _lens = right - left + 1
            if _lens > longest:
                longest = _lens
                res = s[left:right+1]
                
            # 这里的right可以修改一下，right = ind + 1,后面也就少了一些操作，而且也可以完全按照前面的代码执行了。    
            left, right = ind, ind
            if right + 1 < lens and s[left] == s[right + 1]:
                right += 1
                _lens = right - left + 1
                if _lens > longest:
                    longest = _lens
                    res = s[left: right+1]
                    
                while(True):
                    left = left - 1
                    right = right + 1
                    if left >= 0 and right < lens and s[left] == s[right]:                     
                        continue
                    else:
                        left += 1
                        right -= 1
                        break
                        
                _lens = right - left + 1
                if _lens > longest:
                    longest = _lens
                    res = s[left:right+1]
                    
        if longest==0:
            return s[0]                    

        return res

    # summary：
    # 上述几种都是中心扩展方法。
    # good solution
    # 这个代码太巧了，和上述代码思路一样，但是简洁。他的start和end位置不是准确位置，而是偏离正确位置一个单位，但是这不影响最终结果。
    # 缺点就是使用关键字str做名字。
    class Solution:
        def longestPalindrome(self, s):
            """
            :type s: str
            :rtype: str
            """
            str = ""
            for i in range(2*len(s)-1):
                if i%2 == 0:
                    start = end = i//2
                    while start>=0 and end<len(s) and s[start]==s[end]:
                        start-=1
                        end+=1
                else:
                    start = (i-1) // 2
                    end = (i+1) //2
                    while start>=0 and end<len(s) and s[start]==s[end]:
                        start-=1
                        end+=1
                if len(str)<=(end-start-1):
                    str=s[start+1:end]
            return str
