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
