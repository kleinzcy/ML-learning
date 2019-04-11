# 思考了很久，没找到第一个方法妙在哪里，按照我的理解，程序的优化建立在减少重复计算上。第二个暴力法也没有重复计算，那么第一个程序好在哪里呢？
# 对A，B遍历，一定要遍历N^2次，而ab_map的长度不一定是N^2。那么第二步循环一定小于N^4.

class Solution(object):
    def fourSumCount(self, A, B, C, D):
        """
        :type A: List[int]
        :type B: List[int]
        :type C: List[int]
        :type D: List[int]
        :rtype: int
        """
        count = 0
        ab_map = dict()
        
        for a in A:
            for b in B:
                ab_map[a + b] = ab_map.get(a + b, 0) + 1
            
        for c in C:
            for d in D:
                s = -(c + d)
                if s in ab_map:
                    count += ab_map[s]
        
        return count
        
 # 暴力法      
 class Solution(object):
    def fourSumCount(self, A, B, C, D):
        """
        :type A: List[int]
        :type B: List[int]
        :type C: List[int]
        :type D: List[int]
        :rtype: int
        """
        A.sort()
        B.sort()
        C.sort()
        D.sort()
        output = 0
        for a in A:
            for b in B:
              for c in C:
                  for d in D:
                    if a+b+c+d>0:
                      break
                    elif a+b+c+d==0:
                      output += 1
                      
        return output
