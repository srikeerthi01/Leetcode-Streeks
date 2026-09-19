class Solution:
    def myAtoi(self, s: str) -> int:

        ans = []
        i = 0
        n = len(s)

    
        while i < n and s[i] == ' ':
            i += 1


        sign = 1
        if i < n and s[i] == '-':
            sign = -1
            i += 1
        elif i < n and s[i] == '+':
            i += 1


        while i < n and s[i].isdigit():
            ans.append(s[i])
            i += 1


        num = 0
        for ch in ans:
            num = num * 10 + int(ch)

        num = num * sign
        if num < -2147483648:
            return -2147483648

        if num > 2147483647:
            return 2147483647

        return num