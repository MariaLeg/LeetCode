# https://leetcode.com/explore/interview/card/top-interview-questions-easy/92/array/564/

class Solution(object):
    def maxProfit(self, prices):
        empty_portfolio = True
        profit = 0
        buy_price = None
        for i in range(len(prices)):
            # if portfolio is empty AND (there is next day) AND the price next day will be higher
            # then we will buy a stock and store buy_price
            if empty_portfolio and i != len(prices) - 1 and prices[i] < prices[i + 1]:
                empty_portfolio = False
                buy_price = prices[i]

            # if we have a stock in portfolio AND
            # (today is the last trading day
            # OR
            # tomorrow the price will be less)
            # then sell the stock and add (sell-buy) to profit
            elif not empty_portfolio and (i == len(prices) - 1 or prices[i + 1] < prices[i]):
                profit += prices[i] - buy_price
                empty_portfolio = True
        return profit


prices = [1, 7, 8]
profit = Solution().maxProfit(prices)
print(profit)
