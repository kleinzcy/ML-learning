# 把这个问题当做插空问题，首先初始化states = ['('*n+')']，然后插入')',时间复杂度比较高，四层循环，很多重复计算，这里我使用集合来避免了重复。
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def generate(states):
            output = set()
            lens = len(states[0])
            for state in states:
                # num1表示(的个数，num2表示)的个数
                num1 = 0
                num2 = 0
                for i in range(lens-1):
                    if state[i]=='(':
                        num1 += 1
                    else:
                        num2 += 1
                    
                    if num1 > num2:
                        temp = state[:i+1]+')'+state[i+1:]
                        _num1 = num1
                        _num2 = num2 + 1
                        for j in temp[i+2:]:
                            if j == '(':
                                _num1 += 1
                            else:
                                _num2 += 1
                                
                            if _num1 < _num2:
                                break
                        else:
                            output.add(temp)
                        
            return list(output)
        
        states = ['('*n+')']
        for i in range(n-1):
            states = generate(states)
            
        return states

    
#递归解法，代码简洁看不懂
# 递归终止条件是字符串的长度达到2*N,left和right记录左括号和右括号的数目。
class Solution(object):
    def generateParenthesis(self, N):
        ans = []
        def backtrack(S = '', left = 0, right = 0):
            if len(S) == 2 * N:
                ans.append(S)
                return
            if left < N:
                backtrack(S+'(', left+1, right)
            if right < left:
                backtrack(S+')', left, right+1)

        backtrack()
        return ans
