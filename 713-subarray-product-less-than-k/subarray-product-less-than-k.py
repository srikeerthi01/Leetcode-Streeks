class Solution(object):
    def numSubarrayProductLessThanK(self, nums, k):
        left,current_product = 0,1
        count = 0
        if k <= 1:
            return 0
        for right in range(len(nums)):
            current_product *= nums[right]
            while current_product >= k: #this checks if the current product increasing k value
                current_product //= nums[left] # dividing because the element is leaving the sldiing window (product window)
                left += 1
            count += right - left + 1
        return count        