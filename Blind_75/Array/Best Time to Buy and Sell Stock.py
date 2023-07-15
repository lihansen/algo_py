# https://leetcode.cn/problems/best-time-to-buy-and-sell-stock/

# You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.
#
# Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0
# only the max profit is needed, not the days.

def maxProfit(prices: list[int]) -> int:
    minprice = float("inf")
    maxprofit = 0
    for price in prices:
        maxprofit = max(price - minprice, maxprofit) # update the maxprofit, previous minprice is used.
        minprice = min(price, minprice)  # update the minprice, check current price and previous minprice.
    return maxprofit


input = [7,1,5,3,6,4]
res = maxProfit(input)
print(res)