class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        zerosCount , maxLength = 0,0 
        left = 0
        for right in range(len(nums)):
            if nums[right] == 0:
                zerosCount += 1
            #Find valid status, until valid shrink
            while zerosCount > k:
                #shrink
                if nums[left] == 0:
                    zerosCount -= 1
                left += 1
                #update max lenght
            maxLength = max(maxLength,right-left+1) 
        return maxLength           