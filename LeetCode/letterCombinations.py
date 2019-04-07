class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return [] 
        numset = []
        digits2str = {'2':'abc','3':'def','4':'ghi','5':'jkl','6':'mno',
              '7':'pqrs','8':'tuv','9':'wxyz'}

        for temp in digits2str[digits[0]]:
            numset.append(temp)
            
        _numset = []
        for i in digits[1:]:
            for j in digits2str[i]:
                for m in numset:
                    _numset.append(m+j)
            numset = _numset.copy()
            _numset = []
        
        return numset
