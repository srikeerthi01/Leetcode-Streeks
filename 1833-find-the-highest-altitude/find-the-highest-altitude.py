class Solution(object):
    def largestAltitude(self, gain):
        Sum = 0
        ans = [0]
        for i in gain:
            Sum += i
            ans.append(Sum)
        return max(ans)
        