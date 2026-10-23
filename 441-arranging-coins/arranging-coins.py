class Solution(object):
    def arrangeCoins(self, n):
        low,high,rows=0,n,0
        while low <= high:
            mid = low+ (high-low)/2
            coins = mid*(mid+1)/2
            if coins <= n:
                rows = mid
            if coins > n:
                high = mid - 1
            else:
                low = mid + 1
        return rows
        