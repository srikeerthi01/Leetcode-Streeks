class Solution(object):
    def subarraySum(self, nums, k):
        seen={0:1}
        cSum,subCnt = 0,0
        for i in nums:
            cSum += i    
            req = cSum -  k
            if req in seen:
                subCnt += seen[req]
            seen[cSum] = seen.get(cSum,0) + 1
        return subCnt    

        
                

        
        