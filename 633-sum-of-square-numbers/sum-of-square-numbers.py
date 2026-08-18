class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        left , right = 0, int(c**0.5)
        while left <= right:
            sqrSum = left*left + right*right
            if sqrSum == c:
                return True
            elif sqrSum < c:
                left +=1
            elif sqrSum > c:
                right -= 1  
        return False              
                    
        