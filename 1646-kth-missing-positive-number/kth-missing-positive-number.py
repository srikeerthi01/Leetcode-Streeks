class Solution(object):
    def findKthPositive(self, arr, k):
        num = 1
        for i in arr:
            while num < i:
                k -= 1
                if k == 0:
                    return num
                num += 1
            num += 1
        return num + k - 1
        
        
        