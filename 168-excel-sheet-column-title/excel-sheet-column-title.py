class Solution(object):
    def convertToTitle(self, columnNumber):
        ans = ""
        while columnNumber > 0:
            columnNumber -= 1
            remainder = columnNumber % 26
            ans = chr(remainder + ord('A')) + ans
            columnNumber //= 26
        return ans
        