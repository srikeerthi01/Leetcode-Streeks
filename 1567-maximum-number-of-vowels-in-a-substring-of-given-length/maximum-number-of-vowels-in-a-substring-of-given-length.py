class Solution(object):
    def maxVowels(self, s, k):
        s=s.lower()
        count,maxVowel = 0,0
        vowels = 'aeiou'
        left= 0
        for right in range(len(s)):
            if s[right] in vowels:
                count += 1
            if right>= k:
                if s[right - k] in vowels:
                        count -= 1
            if right >= k - 1:
                    maxVowel = max(maxVowel,count)        
                    
                    

           
        return maxVowel        
                

        
                            
       
            
        
        