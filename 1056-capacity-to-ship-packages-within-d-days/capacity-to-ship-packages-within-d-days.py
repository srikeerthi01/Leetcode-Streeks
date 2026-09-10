def canShip(weights,days_have,capacity):
    days_needed = 1
    Sum = 0
    for i in weights:
        if Sum + i <= capacity:
            Sum += i
        else:
            days_needed += 1
            Sum = i
    return days_needed <= days_have
#the above function is the feasabiltiy function
    
class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        low,high = max(weights),sum(weights)
        
        while low < high:
            mid = (low+high)//2
            if canShip(weights,days,mid):
                high = mid
            else:
                low = mid + 1
        return low
        