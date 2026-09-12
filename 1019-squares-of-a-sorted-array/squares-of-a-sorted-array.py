class Solution(object):
    def sortedSquares(self, nums):
        nums.sort()
        ans= []
        for i in nums:
            ans.append(i*i)
        ans.sort()
        return ans
            
        