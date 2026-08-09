class Solution:
    def maxArea(self, height: List[int]) -> int:
        maxWater = 0
        left = 0
        right = len(height) - 1
        while left < right:
            width = right - left
            containerHeight = min(height[left],height[right])
            water = width*containerHeight
            if maxWater < water:
               maxWater = water
            if height[left] < height[right]:
               left+=1
            else:
                right -= 1
        return maxWater    
        