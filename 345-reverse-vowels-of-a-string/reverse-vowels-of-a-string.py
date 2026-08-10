class Solution(object):
    def reverseVowels(self, s):
        s=list(s)
        left,right=0,len(s)-1
        v = "aeiouAEIOU"
        while left < right:
            if  s[left] in v and s[right] in v:
                s[left],s[right] = s[right],s[left]
                left+=1
                right-=1
            elif s[left] in v and s[right] not in v:
                right -= 1
            elif s[left] not in v and s[right] in v:
                left += 1
            elif s[left] not in  v and s[right] not in v:
                left += 1
                right -= 1
        return ''.join(s)                  
       
        