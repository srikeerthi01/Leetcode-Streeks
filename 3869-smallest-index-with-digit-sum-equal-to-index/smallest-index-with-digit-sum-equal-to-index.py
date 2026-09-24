class Solution:
    def smallestIndex(self, nums: List[int]) -> int:
        
        for i in range(len(nums)):
            digit_sum = 0
            while nums[i] > 0:
                digit = nums[i] % 10
                digit_sum += digit
                nums[i] = nums[i]//10
            if digit_sum == i:
                return i
        return -1

               
        

        