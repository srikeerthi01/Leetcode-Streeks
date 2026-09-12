class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        answer = [1]*n
        left = 1
        for i in range(n):
            answer[i] = left
            left *= nums[i]
        right = 1
        for i in range(n-1,-1,-1):
            answer[i] *= right
            right *= nums[i]
        return answer
#the logic is that answer [i] = left_array* right_array , we don't use division here
        