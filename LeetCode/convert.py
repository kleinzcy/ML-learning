# my solution 1： 120ms,6.6MB
# 按行数遍历，根据同一行字符的index关系，将字符依次从s中取出
class Solution:
    def convert(self, s: 'str', numRows: 'int') -> 'str':
        lens = len(s)
        res = ""
        indlist = []
        if numRows==1:
            return s
        
        for row in range(numRows):
            if row == 0:
                i = 0
                ind = 0
                while(ind <= lens - 1):
                    indlist.append(ind)
                    res += s[ind]
                    i += 1
                    ind = i*2*(numRows - 1 - row)

            elif row != numRows - 1:
                for _ind, num in enumerate(indlist):
                    _num = num + 1
                    if _num < lens:
                        indlist[_ind] = _num
                        res += s[_num]
                        if _num + 2*(numRows - 1 - row) + 1 <= lens:
                            res += s[_num + 2*(numRows - 1 - row)]
                            
            else:
                for _ind, num in enumerate(indlist):
                    _num = num + 1
                    if _num < lens:
                        indlist[_ind] = _num
                        res += s[_num]
                
        return res            
  
  
#my solution 2: 104ms,6.6MB
#遍历字符串s,依次将字符放入对应的行，最后将这些行拼接起来。
# 优点：相比于之前的代码，速度提高了，而且更加简洁。主要难点在于，goingdown这个变量的维护，将这个变量的变化把控住，就简单了。
class Solution:
    def convert(self, s: 'str', numRows: 'int') -> 'str':
        lens = len(s)
        res = ""
        rowdict = {}
        if numRows==1:
            return s
        
        goingdown = True
        
        currentrow = 0
        for c in s:
                
            if currentrow not in rowdict:
                rowdict[currentrow] = c
            else:
                rowdict[currentrow] += c
                
            if currentrow + 1 == numRows and goingdown:
                goingdown = False
                
            if currentrow == 0 and not goingdown:
                goingdown = True
                
            currentrow += (1 if goingdown else -1)
                
        for row in range(min(numRows, lens)):
            res += rowdict[row]           
        
        return res  
        
        
# good solution: 92ms
class Solution:
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1:
            return s
        zigzag = ['' for i in range(numRows)]  # 初始化zigzag为['','','']
        row = 0                                # 当前的行数
        step = 1                               # 步数：控制数据的输入
        for c in s:
            if row == 0:
                step = 1
            if row == numRows - 1:
                step = -1
            zigzag[row] += c
            row += step
        return ''.join(zigzag)
        
 # summary:第三种方法，少了很多判断，用step替代了方法二中的bool类型，此外，这里使用list类型来存储数据，相比我用字典，差别不大，关键是，
 # 字典每次都要判断键值，这就有点多余。
