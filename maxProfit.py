#You are given an array where prices[i] is the price of a given stock on day i.
#You want to maximize your profit by choosing a single day to buy one stock and choosing a
#different day in the future to sell that stock.


def maxProfit(prices):
    min_price = float('inf')
    max_profit = 0
    for price in prices:
        min_price = min(min_price, price)
        max_profit = max(max_profit, price- min_price)
    return max_profit
