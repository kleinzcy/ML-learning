# 将三数之和问题化成两数之和问题。此外，定位绝对值最小的位置，进一步简化程序，只用set去重，用list会超时。
# 这次，我感觉到了算法能力的进步。加油，知道简化这个问题，没有尝试暴力搜索。
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:    
        nums.sort()
        lens = len(nums)
        if lens<3:
            return []
        
        abslist =  list(map(abs, nums)) 
        minindex = abslist.index(min(abslist))
        if minindex + 2 <= lens-1 and nums[minindex+2]==0:
            minindex += 2
            
        del abslist
        left = 0
        right = 0
        ans = set()
        for index in range(minindex+1):
            left = index + 1
            right = lens - 1
            
            while(left<right):
                threesum = nums[index]+nums[left]+nums[right]
                if threesum==0:
                    ans.add((nums[index],nums[left],nums[right]))
                    while left < right and nums[right] == nums[right-1]:
                        right -= 1
                    while left < right and nums[left] == nums[left +1]:
                        left += 1
                    right -= 1
                    left += 1

                elif threesum > 0:
                    while left < right and nums[right] == nums[right-1]:
                        right -= 1
                    right -= 1
                else:
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    left += 1
                
        return list(ans)
