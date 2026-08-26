class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        idx = -1
        ans = []
        for i in range(len(word)):
            ans.append(word[i])
            if word[i] == ch:
                idx=i
                break
        if idx == -1:
            return word
        s = "".join(ans)
        return s[::-1] + word[idx+1:]
           
        