class Solution(object):
    def maxSubArray(self, nums):
        max_ = nums[0]
        current_sum = nums[0]
        for i in range(1,len(nums)):
            current_sum = max(nums[i],current_sum+nums[i])
            if current_sum > max_:
                max_ = current_sum
        return max_
        
       
        