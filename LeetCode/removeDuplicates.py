# 一开始，我的做法是，从nums中移除重复的元素，移除操作比较耗时。
# 官方给的是交换值，将不重复的元素移到数组前面。这个方法太好了
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 
        i = 0
        for j in range(len(nums)-1):
            if nums[i]!=nums[j+1]:
                i += 1
                nums[i]=nums[j+1]
                
        return i+1
