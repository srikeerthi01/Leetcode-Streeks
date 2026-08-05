class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        maxAverage = -10000000
        left = 0
        currentSum = 0
        for right in range(len(nums)):
            currentSum += nums[right]
            if right >= k - 1:
                avg = currentSum / k
                maxAverage = max(avg, maxAverage)
                #subtracting the value on left as array moves forward
                currentSum -= nums[left]
                left += 1
        return maxAverage         
        