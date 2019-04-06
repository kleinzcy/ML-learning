# 排序后，双指针
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        
        left = 0
        right = 0
        res = float('Inf')
        for now in range(len(nums)-2):
            left = now + 1
            right = len(nums) - 1
            
            while(left < right):
                threesum = nums[now] + nums[left] + nums[right]
                temp = threesum-target
                if abs(res-target)  > abs(temp):
                    res = threesum

                if temp>0:
                    right -= 1
                elif temp<0:
                    left += 1
                else:
                    return res
        return res
