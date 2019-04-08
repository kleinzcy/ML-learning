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
