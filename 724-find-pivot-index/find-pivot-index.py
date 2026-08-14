class Solution(object):
    def pivotIndex(self, nums):
        prefix_sum = [0]
        sum_ = 0
        for i in range(len(nums)):
            sum_ += nums[i]
            prefix_sum.append(sum_)   
        for i in range(len(nums)):
            left_sum = prefix_sum[i]
            right_sum = prefix_sum[len(nums)] - prefix_sum[i+1]
            if left_sum == right_sum:
                return i
        return -1        

           
          
       
        