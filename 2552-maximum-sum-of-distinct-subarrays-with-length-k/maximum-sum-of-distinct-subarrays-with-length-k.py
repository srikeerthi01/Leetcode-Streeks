class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        d = {}
        maxSum,left,currentSum = 0,0,0
        for right in range(len(nums)):
            currentSum += nums[right]
            d[nums[right]] = d.get(nums[right],0) + 1
            if right >= k:
                currentSum -= nums[left]
                d[nums[left]] -= 1
                if d[nums[left]] == 0:
                  del d[nums[left]]
                left += 1
               
            if right >= k - 1:
                if len(d) == k:
                    maxSum = max(maxSum,currentSum)
        return  maxSum

            