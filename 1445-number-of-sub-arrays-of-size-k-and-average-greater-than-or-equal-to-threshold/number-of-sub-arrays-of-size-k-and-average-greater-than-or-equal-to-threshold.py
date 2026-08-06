class Solution(object):
    def numOfSubarrays(self, arr, k, threshold):
        maxAverage = -1000000
        left = 0
        currentSum = 0
        count = 0
        for right in range(len(arr)):
            currentSum += arr[right]
            if right >=  k - 1:
                 avg = currentSum/k
                 if avg >= threshold:
                    count += 1
                 currentSum -= arr[left]
                 left += 1
        return count        
                 
                  
                  
            
               
        