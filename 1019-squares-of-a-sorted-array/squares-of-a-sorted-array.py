class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        ans = []
        for i in nums:
            ans.append(i*i)
        ans = sorted(ans)
        return ans 
       
        