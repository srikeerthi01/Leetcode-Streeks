class Solution(object):
    def maximumWealth(self, accounts):
        max_wealth = 0
        for coustmer in accounts:
            wealth = sum(coustmer)
            if wealth > max_wealth:
                max_wealth = wealth
        return max_wealth        

        
        