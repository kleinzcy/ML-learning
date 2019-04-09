class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return
        
        front = nums[0]
        dup = 1
        for j in nums[1:]:
            if j==front:
                dup += 1
                if dup>2:
                    nums.remove(front)
                    dup -= 1
            else:
                front = j
                dup = 1
                
# 代码简洁   这个题目的允许两个字符重复，所以i-2
# 下面两种方法的i意义不同，第一种方法中，i代表要插入数据的位置，而第二个i代表上一个插入数据的位置
# 这两个题，给我一些启发。一、列表中重复字符的处理。二、实现一个算法前，要明确每一个变量的实际意义，
# 只有这样，整个程序才会顺畅，简洁，不应该边做边创建变量，而是在动手之前就想好需要那些变量。
class Solution:
    def removeDuplicates(self, nums):
            """
            :type nums: List[int]
            :rtype: int
            """
            i = 0
            for e in nums:
                if i < 2 or e != nums[i - 2]:
                    nums[i] = e
                    i += 1

            return i

class Solution:
    def removeDuplicates(self, nums):
            """
            :type nums: List[int]
            :rtype: int
            """
            if not nums:
                return 
            i = 0
            for e in nums[1:]:
                if i < 1 or e != nums[i - 1]:
                    i += 1
                    nums[i] = e

            return i+1
