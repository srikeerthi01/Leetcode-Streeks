class Solution(object):
    def firstStableIndex(self, nums, k):
        n = len(nums)
        for i in range(n):
            max_score = max(nums[0:i+1])
            min_score = min(nums[i:n])
            score = max_score - min_score
            if score <= k:
                return i
        return -1        
#for this problem, we need to find the max from 0 to i and min from i to n (which is the end of array length) and  we need to find their difference and if the difference is less than or equal to the given k value , return the index , where the condition is satisfied .
        