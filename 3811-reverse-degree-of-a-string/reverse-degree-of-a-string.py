class Solution:
    def reverseDegree(self, s: str) -> int:
        reverse = []
        for ch in range(1,len(s)+1):
            ans = (122 - ord(s[ch-1]) + 1)*ch  #here we are using 1 based index but srtings usually ahve 0 based index so, we wrote s[ch-1] to get the correct character in teh index
            reverse.append(ans)
        return sum(reverse)
        