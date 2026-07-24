class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # check if subsequent num is greater than current
        # if it's greater, set buy point
        # find the difference between the two
        # store that as current max and update global max if needed
        # then check again and repeat
        # if the subsequent num is smaller, skip the iteration
        buy = prices[0]
        profit = 0
        current = 0

        for i in range(len(prices)):
            if prices[i] < buy:
                buy = prices[i]
            
            if prices[i] > buy:
                current = prices[i] - buy
            
            if current > profit:
                profit = current
        
        return profit

            
